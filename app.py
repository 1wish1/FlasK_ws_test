from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/base')
def home():
    return render_template('base.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return f"User : {username}"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/hello")
def hello():
    return "<p> hehheh </p>"


@app.route('/forms_basic')
def forms_basic():
    return render_template('forms-basic.html')

@app.route('/')
@app.route('/forms')
def forms():
    return render_template('forms.html')


@app.route('/products')
def products():
    products = ["asd", "qwe","zxc"]
    products_list = "<ul>" 
    for product in products:
        products_list += f"<li>{product}</li>"
    products_list +="</ul>"
    return "list of product: <br>" + products_list



if __name__ == '__main__':
    app.run(debug=True)