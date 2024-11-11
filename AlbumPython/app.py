from flask import Flask
from config import Config
from extensions import db  
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app) 
migrate = Migrate(app, db)

from routes import main as main_blueprint
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
