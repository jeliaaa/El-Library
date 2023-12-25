from flask import render_template, redirect, request, jsonify, flash
from forms import AddLibraryForm, AddBookForm, EditLibraryForm, RegistrationForm, LoginForm
from os import path
from ext import db, app
from models import Library, Book, User
from flask_login import login_user, logout_user, login_required, current_user
@app.route('/')
def index():
    librariess = Library.query.all()
    return render_template("main.html", libraries=librariess)
@app.route('/addBook/<int:libraryId>', methods=["GET", "POST"])
@login_required
def AddBook(libraryId):
    library = Library.query.get(libraryId)
    libraryAdmin = library.libAdminUsername == current_user.username
    if current_user.role != 'libAdmin' or not libraryAdmin:
        return redirect('/adminLoginErr')
    form = AddBookForm()
    if(form.validate_on_submit()):
        newBook = Book(bookImg=form.bookImg.data.filename, bookName=form.bookName.data, bookDescription=form.bookDescription.data, bookAuthor=form.bookAuthor.data, library_id=libraryId)
        db.session.add(newBook)
        db.session.commit()
        fileDirectory = path.join(app.root_path, "static", form.bookImg.data.filename)
        form.bookImg.data.save(fileDirectory)
        return redirect('/MyLibrary')
    return render_template("add.html", form=form)
@app.route('/addLib', methods=["GET", "POST"])
@login_required
def AddLib():
    if current_user.role != 'mainAdmin':
        return redirect('/adminLoginErr')
    form = AddLibraryForm()
    if (form.validate_on_submit()):
        newLibAdmin = User(username=form.libraryAdminUsername.data, password=form.libraryAdminPass.data, mail=form.libraryAdminEmail.data, role='libAdmin')
        user = User.query.filter(User.username == newLibAdmin.username).first()
        if user:
            flash('Username already exists. Please choose a different username.', 'danger')
        else:
            newLib = Library(libName=form.libraryName.data, libDescription=form.libraryDescription.data,
                             libAddress=form.libraryAddress.data, libPhone=form.libraryPhone.data,
                             libImg=form.libraryImg.data.filename, libPrice=form.libraryPrice.data,
                             libAdminUsername=form.libraryAdminUsername.data)
            db.session.add(newLib)
            db.session.commit()
            fileDirectory = path.join(app.root_path, "static", form.libraryImg.data.filename)
            form.libraryImg.data.save(fileDirectory)
            db.session.add(newLibAdmin)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect('/')
    return render_template("addLib.html", form=form)

@app.route('/library/<int:library_id>')
def lib_single(library_id):
    chosen_library = Library.query.get(library_id)
    if not chosen_library:
        return render_template('<div>ERROR</div>')
    return render_template("libsingle.html", library=chosen_library, admin=False)

@app.route('/edit_library/<int:library_id>', methods=["GET", "POST"])
@login_required
def edit_library(library_id):
    chosen_library = Library.query.get(library_id)
    if current_user.role != 'libAdmin' or chosen_library.username != current_user.username:
        return redirect('adminLoginErr.html')
    if not chosen_library:
        return render_template('<div>ERROR</div>')
    form = EditLibraryForm(libraryName=chosen_library.libName, libraryDescription=chosen_library.libDescription, libraryAddress=chosen_library.libAddress, libraryPhone=chosen_library.libPhone, libraryImg=chosen_library.libImg, libraryPrice=chosen_library.libPrice)
    if form.validate_on_submit():
        chosen_library.libName = form.libraryName.data
        if(form.libraryImg.data != chosen_library.libImg):
            chosen_library.libImg = form.libraryImg.data.filename
        else:
            pass
        chosen_library.libDescription = form.libraryDescription.data
        chosen_library.libAddress = form.libraryAddress.data
        chosen_library.libPhone = form.libraryPhone.data
        chosen_library.libPrice = form.libraryPrice.data
        db.session.commit()
        return redirect('/')
    return render_template("addLib.html", form=form, edit=True)
@app.route('/delete_library/<int:library_id>')
@login_required
def delete_library(library_id):
    if current_user.role != 'mainAdmin':
        return redirect('adminLoginErr.html')
    chosen_library = Library.query.get(library_id)
    if not chosen_library:
        return render_template('<div>ERROR</div>')
    db.session.delete(chosen_library)
    db.session.commit()
    return redirect('/')
@app.route('/delete_book/<int:libID>/<int:bookID>')
@login_required
def delete_book(libID,bookID):
    choosen_library = Library.query.get(libID)
    chosen_book = Book.query.get(bookID)
    if current_user.role != 'libAdmin' or choosen_library.libAdminUsername != current_user.username:
        return redirect('adminLoginErr.html')
    if not chosen_book:
        return render_template('<div>ERROR</div>')
    db.session.delete(chosen_book)
    db.session.commit()
    return redirect('/MyLibrary')
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        newUser = User(username=form.username.data, password=form.password.data, role='user', mail=form.email.data)
        user = User.query.filter(User.username == newUser.username).first()

        if user:
            flash('Username already exists. Please choose a different username.', 'danger')
        else:
            db.session.add(newUser)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect('/')

    return render_template("register.html", form=form)
@app.route('/login')
def login():
    return render_template("login.html")
@app.route('/login/user', methods=["GET", "POST"])
def userLogin():
    form = LoginForm()
    if form.validate_on_submit():
        # Use first() to get the user instance
        user = User.query.filter(User.username == form.username.data).first()
        print("Username:", form.username.data)
        print("Password:", form.password.data)
        print("User:", user.username, user.password, user.check_pass(form.password.data))
        if user and user.check_pass(form.password.data):
            login_user(user)
            return redirect('/')
        else:
            # Use return to actually redirect
            return redirect('/ara')

    return render_template("userLogin.html", form=form)

@app.route('/login/library_admin', methods=["GET", "POST"])
def adminLogin():
    form = LoginForm()
    if (form.validate_on_submit()):
        user = User.query.filter(User.username == form.username.data).first()
        if(user and user.check_pass(form.password.data)):
            login_user(user)
        return redirect('/')
    return render_template("adminLogin.html", form=form)
@app.route('/log_out')
def logOut():
    logout_user()
    return redirect('/')
@app.route('/MyLibrary')
@login_required
def view_library():
    # Check if the current user has the 'libAdmin' role
    if current_user.role == 'libAdmin':
        # Fetch the library based on the admin username
        library = Library.query.filter_by(libAdminUsername=current_user.username).first()
        if library:
            # User has access to the library, perform actions or render the library page
            return render_template("libsingle.html", library=library, admin=library)
        else:
            # User is 'libAdmin' but not associated with any library
            return render_template('error.html', message='You are not the admin of any library.')
    else:
        # User doesn't have the 'libAdmin' role
        return render_template('error.html', message='You do not have the required role to access this page.')
@app.route('/searchPage')
def searchPage():
    return render_template("search.html")
@app.route('/search/libraries')
def searchLibs():
    return render_template("searchLibraries.html")
@app.route('/search/books')
def searchBooks():
    return render_template("searchBooks.html")
@app.route('/searchb', methods=['POST', 'GET'])
def searchb():
    query = request.form.get('query', '')
    results = Book.query.filter(Book.bookName.ilike(f'%{query}%')).all()
    books = [{'id': book.BookID, 'name': book.bookName, 'img': book.bookImg, 'description': book.bookDescription, 'author' : book.bookAuthor} for book in results]
    return jsonify({'books': books})
@app.route('/searchl', methods=['POST', 'GET'])
def searchl():
    query = request.form.get('query', '')
    results = Library.query.filter(Library.libName.ilike(f'%{query}%')).all()
    libraries = [{'id': library.LibID, 'name': library.libName, 'img': library.libImg, 'description': library.libDescription, 'admin': library.libAdminUsername} for library in results]
    return jsonify({'libraries': libraries})

@app.route('/adminLoginErr')
def adminErr():
    return render_template('adminLoginErr.html')
@app.route('/about-us')
def about():
    return render_template('aboutUs.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')