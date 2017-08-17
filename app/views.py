from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<user>')
def index(user='None'):
    return "Request Method: %s" % request.method

@app.route('/home/<user_name>')
def home(user_name=None):
    shopping_list = ["cheese","tune","the"]
    return render_template("home.html", name = user_name, i = 1,
    shopping_list = shopping_list)

@app.route('/post/<int:post_id>')
def post(post_id):
    return "Post Id is %s" %post_id

@app.route('/bacon',methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "You are using GET"
    else:
        return "You are using POST"

if __name__=="__main__":
    app.run(debug=True)

    