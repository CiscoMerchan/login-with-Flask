from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField
"""For wtforms.validators.Email becomes active on its functionality. Validates an email address. 
Requires email_validator package to be installed. For ex: pip install wtforms[email]."""
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators={DataRequired(),
                                                           Length(min=8, max=20,
                                                                  message="Password need to be minimum 8 characters")})
    submit = SubmitField(label='Submit')
app = Flask(__name__)
Bootstrap(app)
"""The ['SECRET_KEY'] number is obtain from the terminal typing first>import secrets (Enter). 
2>secrets.token_urlsafe(16) (Enter). and the OUTPUT in this case is '2MMqyZ4WWa07pwCAEJWb3A'"""
app.config['SECRET_KEY'] ='2MMqyZ4WWa07pwCAEJWb3A'

@app.route("/")
def home():
    return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        print(login_form.email)
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html',form=login_form)

if __name__ =='__main__':
    app.run(debug=True)
