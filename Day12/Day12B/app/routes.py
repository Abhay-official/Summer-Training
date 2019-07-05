from app import app
@app.route('/')
@app.route('/abhinav')
@app.route('/index')
def index():
    user={'username':'Abhinav'}
    skill="Python,C,C++"
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello '''+ user['username']+''' u r skilled in '''+skill+''' </h1>
    </body>
</html>'''

