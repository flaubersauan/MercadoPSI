from flask import * 
from flask_login import * 
from flask_bcrypt import *

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

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1:3306/mercadopsi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    try:
        db.create_all()
        print("Banco de dados criado!")
    except Exception as e:
        print("Erro ao criar o banco de dados:", e)
        print("Certifique-se de que o servidor MySQL está em execução e as credenciais estão corretas.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash('E-mail já cadastrado.')
            return redirect(url_for('register'))
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash('Cadastro realizado com sucesso. Faça login.')
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
        else:
            flash('E-mail ou senha incorretos.')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard')
@login_required 
def dashboard():
    return render_template('dashboard.html')

#Quando tivermos o dashboard o logout será util

# @app.route('/logout')
# @login_required
# def logout():
#    logout_user()
#    flash('Você foi desconectado.')
#    return redirect(url_for('index'))

# um arq .env (sugestao )
