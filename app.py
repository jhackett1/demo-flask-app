from flask import Flask, render_template, request

app = Flask(__name__)

appName = "My app"

# Home page
@app.route('/')
def hello():
    return render_template('index.html', appName=appName)

# Form submission handler
@app.route('/submit-here', methods=['POST'])
def handle_form():
    email = request.form['email']
    return render_template('result.html', appName=appName, email=email)