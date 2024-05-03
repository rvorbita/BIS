from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import RegistrationForm,EntryForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('entry.html')



@app.route('/entry')
def add_entry():
    
    form = EntryForm()

    if form.validate_on_submit():
        #create a new entry object to db.
        entry = Entry(firstname=form.firstname.data, lastname=form.lastname.data, middlename=form.middlename.data, age=form.age.data, address=form.address.data)
        db.session.add(entry)
        db.session.commit()
        flash('Entry addedd successfully')
    return render_template('entry.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Process user data (e.g., hash password, store in database)
        flash('Thanks for registering!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


