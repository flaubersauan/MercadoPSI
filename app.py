from flask import * 
from flask_login import * 
from bcrypt import * 

app = Flask(__name__)

# cria a parte de config variavel 

# criação das rotas 

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastro')
def register():
    return render_template('cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')

# um arq .env (sugestao )



