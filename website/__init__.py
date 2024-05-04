from flask import Flask

def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asldfkjA2112asiutlkkk:.123&91##LKJA,,cD LA*7)@39'
    
    from .views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    
    return app