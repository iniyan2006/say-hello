from flask import Flask , render_template, request, flash
app = Flask(__name__, template_folder='template')
app.secret_key = "helloworld2006@2006"
@app.route('/')
def index():
    flash('what is your name?')
    return render_template('index.html')
@app.route('/greet', methods = ['POST','GET'])
def greet():
    flash("Hi " + str(request.form['name_input']) + " ,great to see you !")
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
