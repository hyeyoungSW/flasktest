from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import User


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    #Make sure that these are valid email addrs format
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=15)])
    #Make sure that password meets the specific length
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=15)])
    password_confirm = PasswordField("Confirme Password", validators=[DataRequired(), Length(min=6, max=15), EqualTo('password')])
    #equalt to password > password confirm should be equal to password above
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=55)])
    submit = SubmitField("Register Now")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another one.")
    # THis function makes sure that emaill matches to the email = StringFie... here
    # SO whenver call it, It has to be  the same filed name
    # Its also case sensitive
    # USer class which is imported
    #Object now recall the actual database call, you check the email inside the database,
    #and grab the first occurence
    # SO if it user is true, IT means email is already existed in DB
    # so raise the error