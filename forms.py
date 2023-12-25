from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField, FileAllowed, FileSize
from wtforms.fields import StringField, TextAreaField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from email_validator import validate_email
class AddLibraryForm(FlaskForm):
    libraryName = StringField("ბიბლიოთეკის სახელი", validators=[DataRequired(message='შეავსეთ ყველა ველი')], render_kw={"autocomplete": "off"})
    libraryDescription = TextAreaField('აგვიღწერეთ: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryAddress = TextAreaField('მისამართი: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryPhone = TextAreaField('ტელ.ნომერი: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryImg = FileField('სურათი: ', validators=[FileSize(max_size=10*1024*1024), FileAllowed(["jpg", "png","jpeg"], message='შეარჩიეთ სწორი ტიპის ფაილი')])
    libraryPrice = IntegerField('ფასი: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryAdminUsername = StringField('ადმინის იუზერნეიმი: ', validators=[DataRequired(message="ბიბლიოთეკას უნდა ჰყავდეს ადმინი")])
    libraryAdminPass = PasswordField('ადმინის პაროლი', validators=[DataRequired()], render_kw={"autocomplete": "off"})
    libraryAdminEmail = StringField('ადმინის მეილი', validators=[DataRequired()])
    submit = SubmitField('დამატება')

class EditLibraryForm(FlaskForm):
    class AddLibraryForm(FlaskForm):
        libraryName = StringField("ბიბლიოთეკის სახელი", validators=[DataRequired(message='შეავსეთ ყველა ველი')])
        libraryDescription = TextAreaField('აგვიღწერეთ: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
        libraryAddress = TextAreaField('მისამართი: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
        libraryPhone = TextAreaField('ტელ.ნომერი: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
        libraryImg = FileField('სურათი: ', validators=[FileSize(max_size=10 * 1024 * 1024),
                                                       FileAllowed(["jpg", "png", "jpeg"],
                                                                   message='შეარჩიეთ სწორი ტიპის ფაილი')])
        libraryPrice = IntegerField('ფასი: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])

class AddBookForm(FlaskForm):
    bookName = StringField("წიგნის სახელი", validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    bookAuthor = StringField("წიგნის ავტორი", validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    bookDescription = TextAreaField('წიგნის მიმოხილვა', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    bookImg = FileField('წიგნის სურათი: ', validators=[FileSize(max_size=10 * 1024 * 1024), FileAllowed(["jpg", "png", "jpeg"], message='შეარჩიეთ სწორი ტიპის ფაილი')])
    submit = SubmitField('დამატება')

class EditLibraryForm(FlaskForm):
    libraryName = StringField("ბიბლიოთეკის სახელი", validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryDescription = TextAreaField('აგვიღწერეთ: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryAddress = TextAreaField('მისამართი: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryPhone = TextAreaField('ტელ.ნომერი: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    libraryImg = FileField('სურათი: ', validators=[FileSize(max_size=10*1024*1024), FileAllowed(["jpg", "png" ,"jpeg"], message='შეარჩიეთ სწორი ტიპის ფაილი')])
    libraryPrice = IntegerField('ფასი: ', validators=[DataRequired(message='შეავსეთ ყველა ველი')])
    submit = SubmitField('დამატება')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')