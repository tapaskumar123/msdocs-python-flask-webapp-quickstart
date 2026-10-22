import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

import time, random

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/api/products')
def products():
    time.sleep(random.uniform(0.1, 0.4))
    return {"items": ["laptop", "phone", "tablet"]}

@app.route('/api/checkout')
def checkout():
    time.sleep(random.uniform(0.5, 2.5))
    if random.random() < 0.3:
        raise Exception("Payment gateway timeout (demo)")
    return {"status": "order placed"}

@app.route('/api/login')
def login():
    if random.random() < 0.2:
        return {"error": "invalid credentials"}, 401
    return {"status": "ok"}

@app.route('/api/report')
def report():
    time.sleep(3)
    return {"report": "ready"}

if __name__ == '__main__':
   app.run()
