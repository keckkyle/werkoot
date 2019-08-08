from app import app
from flask import render_template
from werkoot_web.blueprints.users.views import users_blueprint
from werkoot_web.blueprints.sessions.views import sessions_blueprint
from werkoot_web.blueprints.measurements.views import measurements_blueprint
from werkoot_web.blueprints.images.views import images_blueprint
from werkoot_web.blueprints.fan_idol.views import fan_idol_blueprint
from werkoot_web.blueprints.comments.views import comments_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(sessions_blueprint,url_prefix="/sessions")
app.register_blueprint(images_blueprint,url_prefix="/images")
app.register_blueprint(measurements_blueprint, url_prefix="/measurements")
app.register_blueprint(fan_idol_blueprint,url_prefix="/fan_idol")
app.register_blueprint(comments_blueprint,url_prefix='/comments')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/")
def home(): 
    return render_template('home.html')
