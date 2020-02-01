from . import *

from PySide2.QtWidgets import QComboBox, QTableWidget, QTableWidgetItem
from PySide2.QtCore import Signal

    

class DBComboBox(QComboBox):
    """
    DBComboBox is extending a QCombobox with an
    SQLAlchemy db object

    dataobject : sqlalchemy db object
    filters    : dict for filtering data object for including 
                 in items of combobox.
                 
                 filters = {
                              'salary' : ('>', 20000), 
                              'name' : ("=", "Alan") 
                           }  


    c1 = DBCombobox(datasession = session, dataobject=City)
    c2 = DBCombobox(datasession = session, dataobject=District)

    c2.setMaster(c1, "districts")   # which we back_populated

    """

    signalMasterId = Signal(object)
    
    def __init__(self, parent, datasession=None, dataobject=None, filters=None, textcolumn=None):
        super(DBComboBox, self).__init__(parent)

    
        
        #TODO: add code to check given columns in filters, idcolumn and textcolumn is present inside model
        try:
            #check existence of attributes 
            pass
        except:
            pass
        
        self.dataobject = dataobject
        self.session = datasession
        self.filters = filters
        self.textcolumn = textcolumn
        self.clear()
        if self.filters is None:
            records = self.session.query(self.dataobject).all()
            for record in records:
                self.addItem(record.__dict__[self.textcolumn], userData=record)
        self.currentIndexChanged.connect(self.idxChanged)
            
    def refill(self,obj):
        self.clear()
        records = self.session.query(self.dataobject).all()
        print(obj.id, obj.name)
        for record in records:
            if (record.__dict__[self.mastercolumn] == obj.id):
                self.addItem(record.__dict__[self.textcolumn], userData=record)
            
                
    def setMaster(self, comboobj, mastercolumn):
        self.mastercolumn = mastercolumn
        self.clear()
        comboobj.signalMasterId.connect(self.refill)

        
    def idxChanged(self):
        print(self.currentIndex())
        self.signalMasterId.emit(self.itemData(self.currentIndex()))

class DBTableWidget(QTableWidget):
    def __init__(self, parent,  datasession=None, dataobject=None):
        super(DBTableWidget,self).__init__(parent)
        
        self.dataobject = dataobject
        self.session = datasession
        self.clear()
        records = self.session.query(self.dataobject).all()

        self.setRowCount(len(records))
        self.setColumnCount(len(self.dataobject.__table__.columns.keys()))

        self.setHorizontalHeaderLabels( self.dataobject.__table__.columns.keys())
        i=0
        for record in records:
            j=0
            for k in self.dataobject.__table__.columns.keys():
                self.setItem(i, j,QTableWidgetItem( str(record.__dict__[k])))
                j+=1
            i+=1
