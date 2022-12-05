from flask import render_template, redirect, url_for, Blueprint, flash
from webse import application
from webse.forward_home.forms import SignUpForm
import boto3

forward_home= Blueprint('forward_home', __name__)

db = boto3.resource('dynamodb', region_name='eu-north-1')
table = db.Table('signuptable')


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
        table.put_item(
            Item={
                'name': form.name.data, 'email': form.email.data,
                'mobile': form.mobile.data, 'country': form.country.data,
                'newsletter': form.newsletter.data
            }
        )    
        msg ='Congratulations! {} is now registered!'.format(form.name.data)
        flash(msg)    
        return redirect(url_for('forward_home.home_page'))
    return render_template('signup.html', form=form)