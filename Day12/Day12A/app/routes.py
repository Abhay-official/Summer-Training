from app import app
@app.route('/')
@app.route('/abhinav')
@app.route('/index')
def index():
    return "Hello World!"
