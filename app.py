from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about')
def about():
    return "This is the About page for application testapp123."

@app.route('/user/<username>')
def user_profile(username):
    return f"Profile page of {username}"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Handle POST request
        name = request.form['name']
        return f"Hello, {name}!"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
