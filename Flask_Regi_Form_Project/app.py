from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisshouldbeasecret'  # Replace with your secret key

# Registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Here, normally save to database
        username = form.username.data
        flash(f'Account created for {username}!', 'success')
        return redirect(url_for('success', username=username))
    return render_template('register.html', form=form)

@app.route('/success/<username>')
def success(username):
    return render_template('success.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
