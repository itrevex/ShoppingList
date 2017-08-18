"""
Script used for rendering views onto the browser
"""
from flask import Flask, request, render_template, redirect, url_for
from customer import Customer, InValidEmailExcpetion, InValidPasswordExcpetion
from shopping_list import ShoppingList

APP = Flask(__name__)
APP.config['DEBUG'] = False

@APP.route('/')
def index():
    return "Request Method: %s" % request.method

@APP.route('/login', methods=['GET', 'POST'])
def login(login_fail=None):
    """
    Method for Linking template and authetication code to 
    Log in user
    """
    if request.method == 'POST':
        if request.form['login'] == "Log In":
            #Log in button has been presssed
            return redirect(url_for('home', user_name="Isaac"))
            try:
                customer = Customer(request.form['email'],request.form['password'])
                if customer.login_status:
                    return redirect(url_for('home', user_name=customer.email))
                else:
                    login_fail = "Wrong Email Or Password"
                    return redirect(url_for('home', user_name=customer.email))

            except (Exception,InValidEmailExcpetion,InValidPasswordExcpetion) as exception:
                customer = Customer(request.form['email'],request.form['password'])
                login_fail = str(exception)

        elif request.form['login'] == "Sign Up":
            #Sign Up button has been placed
            return redirect(url_for('register'))
        else:
            return render_template('login.html', login_fail="Form Failed")
        
    return render_template('login.html', login_fail=login_fail)
    

@APP.route('/home/<user_name>')
def home(user_name=None):
    """
    Function opens home page
    Home page displays the user shopping lists
    """

    shopping_list = ["cheese","tune","the"]
    return render_template("home.html", name = user_name, i = 1,
    shopping_list = shopping_list)

@APP.route('/register')
def register():
    """
    Opens registeration page
    """
    return render_template('register.html')

if __name__=="__main__":
    """
    start app only through main
    """
    APP.run(debug=True)

    