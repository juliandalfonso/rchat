from flask import Flask, render_template, redirect, url_for

from flask_login import LoginManager, login_user, current_user, login_required, logout_user

from passlib.hash import pbkdf2_sha256

from wtform_fields import *
from models import *

# Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# Configure db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tvduqqvnejtcxa:e8eb77ff53c7b0b4ddb07fd495815186243466a012ef03b24984ea342b4fabc8@ec2-107-22-224-154.compute-1.amazonaws.com:5432/d9ghma237tt9pc'

db = SQLAlchemy(app)

# Configure flask login
login = LoginManager(app)
login.init_app(app)


@login.user_loader
def load_user(id):

    return User.query.get(int(id))


@app.route('/', methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()
    # updated db if validation is succesfull
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        hashed_pswd = pbkdf2_sha256.hash(password)

        # Add user to database
        user = User(username=username, password=hashed_pswd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('index.html', form=reg_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    # Allow if validation success
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(
            username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))

    return render_template('login.html', form=login_form)


@app.route("/chat", methods=["GET", "POST"])
@login_required
def chat():
    if not current_user.is_authenticated:
        return "Porfavor inicia sesion para poder chatear"
    return "Chat with me"


@app.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return "Logout succesfull"


if __name__ == '__main__':
    app.run(debug=True)
