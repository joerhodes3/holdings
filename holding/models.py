from sqlalchemy import Column, FLoat, String, Date, Bolean, ForeignKey
#from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from datetime import date

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

    date = Column(Date, default=date.today())
    price = Column(Float, default=0.0)
    quantity = Column(Float, default=0.0)
    
    is_active = Column(Boolean, unique=False, default=True) # mark "False" when I no longer have (sell or lose)

    # notes to help me
    exchange_purchased_on = Column(String)
    currenly_held_on = Column(String)
        
# NOTE: loss is just a sell of $0
# sell -- querry have.symbol.ordered_by.date to find FIFO based sale -- oldest eligable until have.quanity satisfied
class event(Base):
    """ SQLAlchemy Model for all events that have occured """

    __tablename__ = "event"
    id = Column(Integer, primary_key=True)
  
# save list from assets
    
# NOTE tax is just a querry of [event]
