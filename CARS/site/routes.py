from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def welcome():
    return render_template("welcome.html")

@site.route('/aboutus')
def about_us():
    return render_template("aboutus.html")

@site.route('/profile')
def profile():
    return render_template("profile.html")