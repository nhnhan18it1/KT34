from sqlalchemy import Column, Integer, DATETIME, String, ForeignKey
from sqlalchemy.orm import relationship
from main import db
import datetime

class Customers(db.Model):
    __tablename__ = "Customers"
    CustomerID = Column(Integer, primary_key=True, autoincrement=True)
    CustomerName = Column(String(255))
    ContactName = Column(String(255))
    Address = Column(String(255))
    City = Column(String(255))
    PostalCode = Column(String(255))
    Country = Column(String(255))
    orders = relationship('Orders', backref='Customers', lazy=True)
    def __init__(self, CustomerName='', ContactName='', Address='',
                 City='', PostalCode='', Country=''
                 ):
        self.CustomerName = CustomerName
        self.ContactName = ContactName
        self.Address = Address
        self.City = City
        self.PostalCode = PostalCode
        self.Country = Country

    @property
    def toString(self):
        return {
            'CustomerID':self.CustomerID,
            'CustomerName':self.CustomerName,
            'ContactName':self.ContactName,
            'Address':self.Address,
            'City':self.City,
            'PostalCode':self.PostalCode,
            'Country':self.Country
        }

class Orders(db.Model):
    __tablename__="Orders"
    OrderID = Column(Integer,primary_key=True,autoincrement=True)
    CustomerID = Column(Integer, ForeignKey(Customers.CustomerID), nullable=False)
    EmployeeID = Column(Integer)
    OrderDate = Column(DATETIME, default=datetime.datetime.now())
    ShipperID = Column(Integer)
    def __init__(self,CustomerId,employeeId,shiperId):
        self.CustomerID = CustomerId
        self.EmployeeID = employeeId
        self.ShipperID = shiperId
    @property
    def toString(self):
        return {
            'OrderID':self.OrderID,
            'CustomerID':self.CustomerID,
            'EmployeeID':self.EmployeeID,
            'OrderDate':self.OrderDate,
            'ShipperID':self.ShipperID
        }

if __name__ == '__main__':
    db.create_all()