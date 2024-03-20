from flask import Flask
#from match_routes import matches_bp
from api.joueur_routes import joueur_bp

app = Flask(__name__)

#app.register_blueprint(matches_bp, url_prefix='/match')
app.register_blueprint(joueur_bp, url_prefix='/joueur')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
