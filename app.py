from flask import * 
from flask_login import * 
from bcrypt import * 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here' 

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 

users = {} 

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email in users:
            flash('Este e-mail já está em uso.')
            return redirect(url_for('register'))

        hashed_password = hashpw(password.encode('utf-8'), gensalt())
        
        users[email] = hashed_password
        
        flash('Cadastro realizado com sucesso! Por favor, faça login.')
        return redirect(url_for('login'))

    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user_hashed_password = users.get(email)

        if user_hashed_password and checkpw(password.encode('utf-8'), user_hashed_password):
            user = User(email)
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('E-mail ou senha incorretos.')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard')
@login_required 
def dashboard():
    return render_template('dashboard.html')


@app.route('/visualizar_carrinho.html')
@login_required 
def visualizar_carrinho():
    return render_template('visualizar_carrinho.html')

#Quando tivermos o dashboard o logout será util

# @app.route('/logout')
# @login_required
# def logout():
#    logout_user()
#    flash('Você foi desconectado.')
#    return redirect(url_for('index'))

# um arq .env (sugestao )
