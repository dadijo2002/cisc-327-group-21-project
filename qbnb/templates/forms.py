"""
This file manages website forms that require
user input.
"""

from flask_wtf import FlaskForm
from qbnb import user_system as qbnbuser

class UpdateProfile(FlaskForm):
    """
    Form to update user profile.
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    billing_address = StringField('Billing Address', validators=[DataRequired()])
    postal_code = StringField('Postal Code', validators=[DataRequired()])
    submit = SubmitField("Update Profile")

    def validate_email(self, email):
        """
        This function validates the email of the user.
        """
        if email.data != current_user.email:
            user = qbnbuser.User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
            else:
                status = qbnbuser.update_email(email)
                if status == False:
                    raise ValidationError('Invalid email format. Please try again.')
                else:
                    return True
    
    def validate_address(self, address):
        """
        This function validates the address of the user.
        """
        if address.data != current_user.billing_address:
            status = qbnbuser.update_address(address)
            if status == False:
                raise ValidationError('Invalid address. Please try again.')
            else:
                return True

    def validate_postal_code(self, postal_code):
        """
        This function validates the postal code of the user.
        """
        if postal_code.data != current_user.postal_code:
            status = qbnbuser.update_postal_code(postal_code)
            if status == False:
                raise ValidationError('Invalid postal code format. Please try again.')
            else:
                return True

