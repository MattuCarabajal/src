from flask import Flask, render_template, send_file
from templates.experience import get_jobs
from templates.presentation import get_ide_data, get_date, get_me_data


app = Flask(__name__)

@app.route( '/' )
def index():
    return render_template( 'index.html' )

@app.route( '/presentation' )
def presentation():
    return render_template( 'presentation.html', ide_data=get_ide_data(), date=get_date(), me=get_me_data() )

@app.route( '/experience' )
def experience():
    return render_template( 'experience.html', jobs=get_jobs() )

def image():
    return send_file('templates/images/profile_foto_rounded.png',  mimetype='image/png')

if __name__ == '__main__':
    app.run( debug=True )