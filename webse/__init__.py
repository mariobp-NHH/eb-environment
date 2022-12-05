from flask import Flask

application = Flask(__name__)


application.config['SECRET_KEY'] = '$ECrEt'



from webse.forward_home.routes import forward_home


application.register_blueprint(forward_home)
