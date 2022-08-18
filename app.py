
from flask import Flask
from config import DevelopmentConfig,ProductionConfig
from models import db
from resources.classrooms import classroom_bp
from resources.alumns import alumn_bp

app = Flask(__name__)

app.config.from_object(ProductionConfig)

app.register_blueprint(classroom_bp)
app.register_blueprint(alumn_bp)

if __name__ == "__main__":
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.run(debug=True)
