from flask import * 
from flask_login import * 
from flask_bcrypt import *
from datetime import datetime

#import os 
# import dotenv
# dotenv.load_dotenv()

from models import (
    db,
    User, 
    Produtos,
    Produtos_Vendidos
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'intercurso2025' 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/mercadopsi'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Rotas básicas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if User.query.filter_by(email=email).first():
            flash('E-mail já cadastrado.')
            return redirect(url_for('register'))
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Cadastro realizado com sucesso.')
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Login realizado com sucesso.')
            return redirect(url_for('dashboard'))
        flash('E-mail ou senha incorretos.')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/adicionar_no_carrinho', methods=['POST'])
@login_required
def adicionar_no_carrinho():
    try:
        nome_produto = request.form.get('nome_produto')
        preco_produto = request.form.get('preco_produto')

        # Criar a nova entrada associada ao usuário logado
        item_carrinho = Produtos_Vendidos(
            nome_produto=nome_produto,
            preco=preco_produto,
            data_venda=datetime.now(),
            usuario_id=current_user.id
        )

        db.session.add(item_carrinho)
        db.session.commit()
        
        flash(f'✅ Produto "{nome_produto}" adicionado ao carrinho com sucesso!')
    
    except Exception as e:
        db.session.rollback()
        flash(f'❌ Erro ao adicionar o produto ao carrinho: {e}')

    return redirect(url_for('visualizar_carrinho'))

@app.route('/visualizar_carrinho')
@login_required
def visualizar_carrinho():
    # Buscar apenas os produtos do usuário logado
    produtos_no_carrinho = Produtos_Vendidos.query.filter_by(usuario_id=current_user.id).all()
    
    total_carrinho = sum(item.preco for item in produtos_no_carrinho)
    
    return render_template('visualizar_carrinho.html', produtos=produtos_no_carrinho, total=total_carrinho)

@app.route('/remover_do_carrinho/<int:produto_id>', methods=['POST'])
@login_required
def remover_do_carrinho(produto_id):
    produto = Produtos_Vendidos.query.filter_by(id=produto_id, usuario_id=current_user.id).first()
    
    if produto:
        db.session.delete(produto)
        db.session.commit()
        flash(f'❌ Produto "{produto.nome_produto}" removido do carrinho.')
    else:
        flash('Produto não encontrado ou não pertence a este usuário.')
    
    return redirect(url_for('visualizar_carrinho'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Você foi desconectado.", "info")
    return redirect(url_for("index"))

#  # um arq .env (sugestao )
if __name__ == "__main__":
    # Cria as tabelas ao iniciar
    with app.app_context():
        db.create_all()
        print("✅ Tabelas criadas com sucesso!")
    app.run(debug=True)
