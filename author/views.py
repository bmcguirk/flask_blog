from flask_blog import app
from flask import render_template, redirect, url_for, session, request
from author.form import RegisterForm, LoginForm
from author.models import Author
from author.decorators import login_required

@app.route('/login', methods=("GET","POST"))
def login():
    form = LoginForm()
    error = None
    
    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)
    else:
        pass
    if form.validate_on_submit():
        author = Author.query.filter_by(
            username = form.username.data,
            password = form.password.data
            ).limit(1)
        if author.count():
            session['username'] = form.username.data
            if 'next' in session:
                next = session.get('next')
                session.pop('next')
                return redirect(next)
            else:
                return redirect(url_for('login_success'))
        else:
            error = "Can't find that username/password combo."
            return render_template('author/login.html', form=form, error=error)
    else:
        return render_template('author/login.html', form=form, error=error)
    
@app.route('/register',methods=('GET','POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    else:
        return render_template('author/register.html', form=form)
        
@app.route('/success')
def success():
    return "Author registered."


@app.route('/login_success')
@login_required
def login_success():
    return "Author logged in."