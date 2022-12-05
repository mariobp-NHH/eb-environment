from flask import render_template, redirect, url_for, Blueprint
from webse import application
from webse.forward_home.forms import SignUpForm
forward_home= Blueprint('forward_home', __name__)


# @forward_home.route('/home')
# @forward_home.route('/')
# def home():
#     return render_template('forward_home/home.html', title='Home')

# @forward_home.route('/developers')
# def developers():
#     return render_template('forward_home/developers.html', title='Developers')

  


@forward_home.route('/')
@forward_home.route('/home')
def home_page():
    return render_template('home.html')


# import redirect, url_form
# from app.forms import SignUpForm 


@forward_home.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        print(
            form.name.data,
            form.email.data,
            form.mobile.data,
            form.country.data,
            form.newsletter.data
        )
        return redirect(url_for('forward_home.home_page'))
    return render_template('signup.html', form=form)