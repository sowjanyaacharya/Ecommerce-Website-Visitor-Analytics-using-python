from flask import Flask  #headerfile
from flask_cors import CORS
from db import db
from landing import landing_blueprint
from dashboard import dashboard_blueprint
app = Flask(__name__)
CORS(app)

#set db config
username = 'root'  #mysql username
password = ''      #mysql p/w
userpass = 'mysql+pymysql://'+username+':'+password+'@'  #splitting the connection string

server = '127.0.0.1'
dbname = '/ecommerce_analytics'

app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True

db.init_app(app)

#Register Blueprint
app.register_blueprint(landing_blueprint)
app.register_blueprint(dashboard_blueprint)

@app.route('/serverstatus') #name comes after domain name(facebook.com/.....)route function gives access
def serverstatus():   #function name can be given by us

    return "server is up and running"

if __name__ == '__main__':  #(it locks server going to respond)app.py is the main file blueprint is linking to the main file(root file)
    app.debug = True
    #app.run()    #to run this on browser http://localhost:5000/serverstatus(on browser),pip install flask-sqlalchemy(terminal),then again pip install pymysql(terminal),then pip install flask-cors
    app.run(debug=True, port=8000)