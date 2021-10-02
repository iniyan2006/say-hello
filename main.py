from flask import Flask , render_template, request, flash
app = Flask(__name__, template_folder='template')
app.secret_key = "helloworld2006@2006"
@app.route('/')
def index():
    flash('hello')
    return render_template('index.html')


app.run(debug=True)