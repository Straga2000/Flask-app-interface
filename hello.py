from flask import Flask, render_template
app = Flask(__name__)

posts = [{'name': 'karen', 'age': 51, 'sex': 'female'}, {'name': 'ben', 'age': 12, 'sex': 'male'}, {'name': 'john', 'age': 31, 'sex': 'male'}]

@app.route('/')
def hello_world():
    return render_template('home.html', posts= posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
