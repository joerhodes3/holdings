from sqlalchemy import Column, FLoat, String, DateTime
#from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime, timedelta

Base = declarative_base()

# Constants
CASCADE_ALL_DELETE = "all, delete"

class have(Base):
    """ SQLAlchemy Model for Assests held """

    __tablename__ = "have"
    id = Column(Integer, primary_key=True)

    # will need some routine at commit to make sure only legal symbols get in
    sybmol = Column(String(10))

    date_bought = Column(DateTime, default=datetime.utcnow)
    total_price_bought = Column(Float, default=0.0)
    quantity_bought = Column(Float, default=0.0)

    # notes to help me
    exchange_purchased_on = Column(String)
    currenly_held_on = Column(String)
        
class sold(Base):
    """ SQLAlchemy Model for Assests sold after being held fo more than 1yr """

    __tablename__ = "sold"
    id = Column(Integer, primary_key=True)
  
    # will need some routine at commit to make sure onl legal symbols get in
    sybmol = Column(String(10))

    # based on matching symbol find date/price
    date_bought = Column(DateTime, default=datetime.utcnow)
    total_price_bought = Column(Float, default=0.0)
    # based on current transaction
    
    date_sold = Column(DateTime, default=datetime.utcnow)
    total_price_sold = Column(Float, default=0.0)
    quantity_sold = Column(Float, default=0.0)

    # try to make long when possible as it is a tax savings
    term = Column(String(5), default="short")

    # notes to help me
    exchange_sold_on = Column(String)
    # save purchasing exchange/held info for posterity
    was_purchased_on = Column(String)
    was_held_on = Column(String)

