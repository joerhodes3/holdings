from sqlalchemy import Column, FLoat, String, DateTime, Bolean, ForeignKey
#from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime, timedelta

Base = declarative_base()

# Constants
CASCADE_ALL_DELETE = "all, delete"

# NOTE: interest GET is just a buy(), where the price is qued as tax to be paid immediately
class have(Base):
    """ SQLAlchemy Model for Assests held """

    __tablename__ = "have"
    id = Column(Integer, primary_key=True)

    # will need some routine at commit to make sure only legal symbols get in ;; bought
    sybmol = Column(String(10))

    date = Column(DateTime, default=datetime.utcnow)
    price = Column(Float, default=0.0)
    quantity = Column(Float, default=0.0)
    
    is_active = Column(Boolean, unique=False, default=True) # mark "False" when I no longer have (sell or lose)

    # notes to help me
    exchange_purchased_on = Column(String)
    currenly_held_on = Column(String)
        
# NOTE: loss is just a sell of $0
# sell -- querry have.symbol.ordered_by.date to find FIFO based sale -- oldest eligable until have.quanity satisfied
class sold(Base):
    """ SQLAlchemy Model for Assests sold based on what have """

    __tablename__ = "sold"
    id = Column(Integer, primary_key=True)
  
    # based on matching symbol find date/price -- fkey back to have()
    bought = Column(Integer, ForeignKey(have.id))
    
    # sold
    date = Column(DateTime, default=datetime.utcnow)
    price = Column(Float, default=0.0)
    quantity = Column(Float, default=0.0)

    # notes to help me
    exchange_sold_on = Column(String)
    
class tax(Base):
    """ SQLAlchemy Model for taxes to be paid """

    __tablename__ = "tax"
    id = Column(Integer, primary_key=True)
  
    # reason either b/c sold_fkey or interest -- have_fkey ;; a non NULL fkey tells you why
    bought = Column(Integer, ForeignKey(have.id), nullable=True)
    sold = Column(Integer, ForeignKey(sold.id), nullable=True)
    
    # short or long? timme held -- try to make long when possible as it is a tax savings
    term = Column(String(5), default="short")
