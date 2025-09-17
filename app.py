from flask import * 
from flask_login import * 
from bcrypt import * 

app = Flask(__name__)

# cria a parte de config variavel 

# criação das rotas 

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('cadastro.html')
    # Errado porém é só pra testar os templates
    return url_for(redirect('index.html'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    # Errado porém é só pra testar os templates
    return url_for(redirect('index.html'))
@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')

# um arq .env (sugestao )



