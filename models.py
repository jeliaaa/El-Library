from ext import db, app, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
class Library(db.Model):
    LibID = db.Column(db.Integer, primary_key=True)
    libName = db.Column(db.String)
    libDescription = db.Column(db.String)
    libAddress = db.Column(db.String)
    libPhone = db.Column(db.String)
    libImg = db.Column(db.String)
    libPrice = db.Column(db.Float)
    libBooks = db.relationship('Book', backref='library', lazy=True)
    libAdminUsername = db.Column(db.String)


class Book(db.Model):
    __tablename__ = 'book'
    BookID = db.Column(db.Integer, primary_key=True)
    bookName = db.Column(db.String)
    bookDescription = db.Column(db.String)
    bookImg = db.Column(db.String)
    bookAuthor = db.Column(db.String)
    library_id = db.Column(db.Integer, db.ForeignKey('library.LibID'), nullable=False)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    mail = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)
    def __init__(self, username, mail, password, role):
        self.username = username
        self.mail = mail
        self.password = generate_password_hash(password)
        self.role = role
    def check_pass(self, password):
        return check_password_hash(self.password, password)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
def create_main_admin():
    admin_username = 'admin'
    admin_email = 'aleksandre.jelia01jr@geolab.edu.ge'
    admin_role = 'mainAdmin'
    # Check if the admin already exists
    existing_admin = User.query.filter_by(username=admin_username).first()
    if existing_admin:
        print("Main admin already exists.")
        for i in User.query.all():
            print(i.username)
            print(i.role)
        return
    # Create the admin user
    admin_password = 'adminadmin'  # Consider using a more secure method
    admin = User(username=admin_username, password=admin_password, mail=admin_email, role=admin_role)
    # Add the admin user to the database
    db.session.add(admin)
    db.session.commit()
    print("Main admin created successfully.")
    print(User.query.all())
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        create_main_admin()