from flask import Flask, render_template, redirect, url_for

from wtform_fields import *
from models import *

# Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# Configure db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tvduqqvnejtcxa:e8eb77ff53c7b0b4ddb07fd495815186243466a012ef03b24984ea342b4fabc8@ec2-107-22-224-154.compute-1.amazonaws.com:5432/d9ghma237tt9pc'

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()
    # updated db if validation is succesfull
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Add user to database
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('index.html', form=reg_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    # Allow if validation success
    if login_form.validate_on_submit():
        return "Logged in, finally"

    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
