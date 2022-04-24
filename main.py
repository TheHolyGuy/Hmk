from flask import render_template, redirect, url_for
from website import auth, create_app

app = create_app()
    
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/Hey', methods=['GET', 'POST'])
def login():
    return render_template('index.html')

@app.route('/end', methods=['GET', 'POST'])
def end():
    return render_template('index.html')

@app.route('/Take-it', methods=['GET', 'POST'])
def sign_up():
    return render_template('index.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return redirect(url_for('index.html'))

if __name__ == '__main__':
    app.run(debug=True)

