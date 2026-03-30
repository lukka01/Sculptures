from flask_wtf import FlaskForm

from wtforms.fields import (StringField, PasswordField, SubmitField)
from wtforms.validators import DataRequired, length, equal_to



class RegisterForm(FlaskForm):
    username = StringField('მიუთითეთ სახელი',
                           validators = [DataRequired()])
    password = PasswordField('მიუთითეთ პაროლი',
                             validators = [DataRequired("განმეორებითი პაროლის ველო სავალდებულოა"), length(min=8, max=64)])
    repeat_password = PasswordField('დაადასტურეთ პაროლი',
                                    validators = [DataRequired(), equal_to("password",
                                                                           message= "პაროლი და განმეორებითი პაროლი არ ემთხვევა!")])
    submit = SubmitField('რეგისტრაცია')


















    #
    # birthday = DateField("მიუთითეთ დაბადების თარიღი",
    #                      validators = [DataRequired()])
    # gender = RadioField("მიუთითეთ გენდერი:", choices=[(0, 'მამაკაცი'), (1, 'ქალბატონი')], validators = [DataRequired()])
    # country = SelectField("მიუთითეთ რეგიონი:", choices=[
    #     "თბილისი",
    #     "რუსთავი",
    #     "თელავი",
    #     "ქუთაისი",
    #     "ვანი",
    #     "ბათუმი"
    # ], validators = [DataRequired()])
    #
    # profile_image = FileField("Upload Profile Image", validators =[FileSize(1024 * 1024), FileAllowed(['jpg', 'png', 'jpeg'])])



    # def validate_password(self, field):
    #     contains_uppercase = False
    #     contains_digit = False
    #     contains_lowercase = False
    #     contains_symbols = False
    #
    #     for char in field.data:
    #         if char in ascii_uppercase:
    #             contains_uppercase = True
    #         if char in digits:
    #             contains_digit = True
    #         if char in ascii_lowercase:
    #             contains_lowercase = True
    #         if char in punctuation:
    #             contains_symbols = True
    #
    #     if not contains_uppercase:
    #         raise ValidationError("პაროლი უნდა შეიცავდეს დიდ ასოებს!")
    #     if not contains_lowercase:
    #         raise ValidationError("პაროლი უნდა შეიცავდეს პატარა ასოებს!")
    #     if not contains_symbols:
    #         raise ValidationError("პაროლი უნდა შეიცავდეს სიმბოლოებს!")
    #     if not contains_digit:
    #         raise ValidationError("პაროლი უნდა შეიცავდეს რიცხვებს!")

