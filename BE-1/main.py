from flask import Flask,jsonify,request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import and_,or_
from flask_cors import CORS
import Model

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://nhav:dnport@localhost:5432/test"

db = SQLAlchemy(app) # Khoi tao sqlalcemy


# GET,POST,PUT,PATCH,DELETE

@app.route('/', methods=['GET'])
def index():
   return "hello!"

@app.route("/home", methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/abc',methods=['GET','POST'])
def abc():
   a = {
       "CustomerID":1,
       "name":"lvminh"
   }
   return jsonify(a)

@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(username,password)
    if username == 'abc' and password == '123':
        return 'success'
    else:
        return 'Fail'

@app.route('/allCustomer',methods=['GET','POST'])
def allCustomer():
    rs = db.session.query(Model.Customers).all()
    rt = []
    for item in rs:
        rt.append(item.toString)
    return jsonify(rt)
    
@app.route('/addCustomer',methods=['POST'])
def addCustomer():
    CustomerName = request.form['CustomerName']
    ContactName = request.form['ContactName']
    Address = request.form['Address']
    City = request.form['City']
    PostalCode = request.form['PostalCode']
    Country = request.form['Country']
    cus = Model.Customers(CustomerName=CustomerName, ContactName=ContactName,
                          Address=Address,City=City,PostalCode=PostalCode,Country=Country)
    db.session.add(cus)
    db.session.commit()
    return "success"

@app.route("/getCustomer/<id>",methods=['GET'])
def getCustomer(id):
    rs = db.session.query(Model.Customers).filter(Model.Customers.CustomerID==id).all()
    response = []
    for item in rs:
       response.append(item.toString)
    return jsonify(response)

@app.route("/getOrderof/<id>",methods=['GET'])
def getOrderof(id):
    rs = db.session.query(Model.Customers).filter(Model.Customers.CustomerID==id).one()
    orders = rs.orders
    return jsonify(orders[0].toString)

if __name__ == '__main__':
    db.create_all()
    app.run(port=5555,host="0.0.0.0",debug=True)