from flask import Flask
from routes import web_routes, api_routes

app = Flask(__name__)

app.register_blueprint(web_routes)
app.register_blueprint(api_routes, url_prefix='/api/user')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
