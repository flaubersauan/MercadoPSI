import os
from app import app, db
from models import Produtos

def inserir_produtos_do_html():
    """
    Lê o arquivo HTML na pasta 'templates', extrai os dados dos produtos e os insere no banco de dados.
    """
    # Constrói o caminho completo para dashboard.html na pasta 'templates'
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_file_path = os.path.join(base_dir, 'templates', 'dashboard.html')

    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo '{html_file_path}' não foi encontrado.")
        return

    # Dividir o conteúdo HTML em blocos de "card" para processar cada produto
    cards = html_content.split('<div class="card">')[1:]
    
    if not cards:
        print("❌ Nenhum produto encontrado no arquivo HTML.")
        return

    produtos_para_inserir = []
    
    for card_content in cards:
        try:
            # Encontrar o nome do produto
            nome_start = card_content.find('<h2>') + len('<h2>')
            nome_end = card_content.find('</h2>', nome_start)
            nome = card_content[nome_start:nome_end].strip()

            # Encontrar o preço do produto
            preco_start = card_content.find('<p>') + len('<p>')
            preco_end = card_content.find('</p>', preco_start)
            preco_str = card_content[preco_start:preco_end].strip()
            
            # Limpar a string do preço para converter em float
            preco_str_limpo = preco_str.replace('R$', '').replace('.', '').replace(',', '.').strip()
            preco = float(preco_str_limpo)
            
            # Criar o objeto e adicionar à lista
            novo_produto = Produtos(nome_produto=nome, preco_produto=preco)
            produtos_para_inserir.append(novo_produto)

        except (ValueError, IndexError) as e:
            print(f"❌ Erro ao processar um card: {e}")
            continue

    # Inserir os produtos no banco de dados
    with app.app_context():
        try:
            db.session.bulk_save_objects(produtos_para_inserir)
            db.session.commit()
            print("✅ Produtos inseridos com sucesso!")
        except Exception as e:
            db.session.rollback()
            print(f"❌ Erro ao inserir produtos no banco de dados: {e}")

# Executa a função
if __name__ == '__main__':
    inserir_produtos_do_html()