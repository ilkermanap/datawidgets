import sys
from PySide2.QtWidgets import QApplication, QDialog

from models import Session, City, District

from datawidgets import DBComboBox, DBTableWidget

s = Session()

from ui_test import Ui_Dialog
class MainWindow(QDialog, Ui_Dialog):
    def __init__(self, app=None):
        super(MainWindow, self).__init__()
        self.app = app
        self.setupUi(self)

        self.city = DBComboBox(self.widget1, datasession=s, dataobject=City, textcolumn="name")
        self.district = DBComboBox(self.widget2, datasession=s, dataobject=District, textcolumn="name")

        self.district.setMaster(self.city, "city_id")

        self.citylist = DBTableWidget(self.widget3, datasession=s, dataobject=City)
        self.show()
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    ret = app.exec_()
    app.exit()
    sys.exit(ret)
