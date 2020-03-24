from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from secrets import token_hex
app = Flask(__name__)

app.config['SECRET_KEY'] = '2f3bf0c271fd404f0e537b162382dcc4'

posts = [{'name': 'karen', 'age': 51, 'sex': 'female'}, {'name': 'ben', 'age': 12, 'sex': 'male'}, {'name': 'john', 'age': 31, 'sex': 'male'}]


@app.route('/')
def hello_world():
    return render_template('home.html', posts= posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"account created for: {form.username.data}!", "success")
        return redirect(url_for('hello_world'))
        #use function name, not app_route
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
    #obj = token_hex(16)
    #print(obj)

