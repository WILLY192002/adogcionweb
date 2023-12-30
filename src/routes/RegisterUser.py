from flask import Blueprint, render_template

main = Blueprint('register_user',__name__)

@main.route('/', methods = ['GET', 'POST'])
def registerUser():
  return render_template('auth/register_user.html')