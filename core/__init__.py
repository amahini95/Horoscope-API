#import Flask class from Flask module we've installed
from flask import Flask
from decouple import config
from flask_restx import Api

#make 'app' object
#where '__name__' arg represents the app's module/package
#so Flask knows where to find other files (like templates)
app = Flask(__name__)
#app configs are set to "APP_SETTINGS", based on the variable in ".env"
app.config.from_object(config("APP_SETTINGS"))
#Make object from "Api" class, pass args to it
api = Api(
    app,
    version='1.0',
    title='Horoscope API',
    description='Get horoscope data easily using the APIs below',
    license='MIT',
    contact='Armin Mahini',
    #contact_url= TODO my personal website,
    #contact_email = TODO hidden email
    #Swagger documentation ('doc') found on the '/' route
    doc='/',
    #'/api/v1' prefixed on each API route
    prefix='/api/v1')

#import routes with this line
from core import routes
