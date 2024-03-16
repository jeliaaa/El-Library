from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileSize
from wtforms.fields import StringField, TextAreaField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
class AddLibraryForm(FlaskForm):
    libraryName = StringField("Library Name", validators=[DataRequired(message='შეავსეთ ყველა ველი')], render_kw={"autocomplete": "off"})
    libraryDescription = TextAreaField('Describe: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryAddress = TextAreaField('Address: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryPhone = TextAreaField('tel.: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryImg = FileField('Image: ', validators=[FileSize(max_size=10*1024*1024), FileAllowed(["jpg", "png","jpeg"], message='შეარჩიეთ სწორი ტიპის ფაილი')])
    libraryPrice = IntegerField('Price: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryAdminUsername = StringField('Admin Username: ', validators=[DataRequired(message="ბიბლიოთეკას უნდა ჰყავდეს ადმინი")])
    libraryAdminPass = PasswordField('Admin Password:', validators=[DataRequired()], render_kw={"autocomplete": "off"})
    libraryAdminEmail = StringField('Admin Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Add')

class EditLibraryForm(FlaskForm):
    class AddLibraryForm(FlaskForm):
        libraryName = StringField("Library", validators=[DataRequired(message='შეავსეთ ყველა ველი')])
        libraryDescription = TextAreaField('Describe: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
        libraryAddress = TextAreaField('Address: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
        libraryPhone = TextAreaField('tel.: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
        libraryImg = FileField('Image: ', validators=[FileSize(max_size=10 * 1024 * 1024),
                                                       FileAllowed(["jpg", "png", "jpeg"],
                                                                   message='შეარჩიეთ სწორი ტიპის ფაილი')])
        libraryPrice = IntegerField('Price: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])

class AddBookForm(FlaskForm):
    bookName = StringField("Book", validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    bookAuthor = StringField("Author", validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    bookDescription = TextAreaField('Description', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    bookImg = FileField('Book Image: ', validators=[FileSize(max_size=10 * 1024 * 1024), FileAllowed(["jpg", "png", "jpeg"], message='შეარჩიეთ სწორი ტიპის ფაილი')])
    submit = SubmitField('Add')


class EditLibraryForm(FlaskForm):
    libraryName = StringField("Library Name", validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryDescription = TextAreaField('Describe: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryAddress = TextAreaField('Address: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryPhone = TextAreaField('tel.: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryImg = FileField('Image: ', validators=[FileSize(max_size=10*1024*1024), FileAllowed(["jpg", "png" ,"jpeg"], message='შეარჩიეთ სწორი ტიპის ფაილი')])
    libraryPrice = IntegerField('Price: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    submit = SubmitField('Add')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enter')