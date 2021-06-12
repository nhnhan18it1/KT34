from sqlalchemy import Integer, String, ForeignKey, Column, DATETIME
from sqlalchemy.orm import relationship
import datetime
import sys
# sys.path.append("..")
from main import db


class Customers(db.Model):
    __tablename__ = "Customer"
    CustomerID = Column(Integer, primary_key=True, autoincrement=True)
    CustomerName = Column(String(255))
    ContactName = Column(String(255))
    Address = Column(String(255))
    City = Column(String(255))
    PostalCode = Column(String(255))
    Country = Column(String(255))
    oders = relationship('Oders', backref='Customer', lazy=True)

    def __init__(self,a=1):
        self.CustomerName = 'a'


class Oders(db.Model):
    __tablename__ = "Order"
    OrderID = Column(Integer, primary_key=True, autoincrement=True)
    CustomerID = Column(Integer, ForeignKey(Customers.CustomerID), nullable=False)
    EmployeeID = Column(Integer)
    OrderDate = Column(DATETIME, default=datetime.datetime.now())
    ShipperID = Column(Integer)

    def __init__(self):
        pass

#
# if __name__ == '__main__':
#     db.create_all()
