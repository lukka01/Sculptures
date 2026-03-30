from flask import render_template, Blueprint
from os import path
from uuid import uuid4

from MyPage.src.views.auth.forms import RegisterForm
from MyPage.src.config import Config

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = {
            "username": form.username.data,
            "password": form.password.data,

        }




    print(form.username.data)
    return render_template("auth/register.html", form = form)