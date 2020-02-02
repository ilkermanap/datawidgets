# datawidgets
PySide2/SqlAlchemy data aware widgets.

Requires PySide2 and SqlAlchemy

To create sqlite test database:

    python3 models.py

Test application with:

    python3 testapp.py
    
## How to Use

For testing purposes, I created two tables with one to many relationship:
            
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
        
Here we have cities, and districts within cities. One city has many districts.

During the ui design with Designer, add Widget where you want to place DBComboBox.

I named widget1, widget2 and widget3 to place my data aware widgets. During the construction of the main window:

    self.city = DBComboBox(self.widget1, 
                           datasession=s, 
                           dataobject=City, 
                           textcolumn="name")
    
above line places a combobox in the place of widget1. Combobox will use a datasession s, and the object name City. 
We explicitly tell which column will be used to display on combobox, which is the "name" column. 
 
Now, we will place our districts combo box. It will be connected with the city combobox:

    self.district = DBComboBox(self.widget2, 
                               datasession=s, 
                               dataobject=District, 
                               textcolumn="name")
                               
    self.district.setMaster(self.city, "city_id")
    
It has the same arguments with the previous city combobox. The next line, with setMaster function, will
use arguments master combobox to connect to, and which column in district object to map to other combobox's id.
 

      