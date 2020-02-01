from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///test.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary = Column(Float)
    
class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    districts = relationship("District")

class District(Base):
    __tablename__ = 'district'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city_id = Column(Integer, ForeignKey('city.id'))
    city = relationship("City", back_populates="districts")
                     

    
if __name__ == "__main__":    
    Base.metadata.create_all(engine)
    s = Session()
    testuser = User(name="ilker", salary=11500.2)
    s.add(testuser)
    s.commit()

    
    c1 = City(id=6,name="Ankara")
    c2 = City(id=34,name="Istanbul")

    d1 = District(name="Beykoz", city_id=34)
    d2 = District(name="Kadikoy", city_id=34)
    d3 = District(name="Silivri", city_id=34)
    d4 = District(name="Cankaya", city_id=6)
    d5 = District(name="Yenimahalle", city_id=6)    
    s.add(c1)
    s.add(c2)
    s.add(d1)
    s.add(d2)
    s.add(d3)
    s.add(d4)
    s.add(d5)
    s.commit()
    
