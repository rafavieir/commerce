from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, db

# Definindo o Blueprint para autenticação
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.validate(username, password)
        if user:
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        flash('Credenciais inválidas.')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Rota para criar novos usuários
@auth.route('/create_user', methods=['GET', 'POST'])
@login_required
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Usuário criado com sucesso!')
        return redirect(url_for('admin.dashboard'))
    return render_template('create_user.html')

# Definindo o Blueprint para a parte principal do site
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/menu')
def menu():
    return render_template('menu.html')

# Definindo o Blueprint para a parte administrativa
admin = Blueprint('admin', __name__)

@admin.route('/admin/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Função para inicializar as rotas
def init_routes(app):
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(admin)
