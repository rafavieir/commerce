from werkzeug.security import generate_password_hash
from models import User, db  # Supondo que db é sua instância SQLAlchemy

# Cria um novo usuário
def create_test_user():
    test_user = User(
        username='admin',
        password=generate_password_hash('password123')  # Substitua 'password123' pela senha desejada
    )
    db.session.add(test_user)
    db.session.commit()

# Execute este código uma vez para criar o usuário de teste
create_test_user()