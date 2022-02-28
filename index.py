from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route( '/' )
def index():
    return render_template( 'index.html' )

@app.route( '/presentation' )
def presentation():
    return render_template( 'presentation.html' )

@app.route( '/experience' )
def experience():
    return render_template( 'experience.html' )

def image():
    return send_file('templates/images/profile_foto_rounded.png',  mimetype='image/png')

if __name__ == '__main__':
    app.run( debug=True )