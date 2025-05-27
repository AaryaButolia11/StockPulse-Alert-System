from flask import Flask, request, render_template, redirect, url_for, flash
import subprocess
import sys

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

@app.route('/', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        stock = request.form['stock']
        phone = request.form['phone']

        # Run scheduler.py with arguments using same Python interpreter
        subprocess.Popen([sys.executable, 'scheduler.py', stock, phone])

        flash('You will be updated!')  # Flash message for notification

        return redirect(url_for('subscribe'))  # Redirect to GET

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
