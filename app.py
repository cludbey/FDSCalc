import csv
from sys import argv, exit
from scipy.spatial import distance
from PyQt5 import QtCore, QtGui, QtWidgets
from fds import Ui_MainWindow

class FDSApp(Ui_MainWindow):
    def __init__(self,QMainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(QMainWindow)
        self.xy_calc_button.clicked.connect(self.CalculateOutput)
        # files = self.file_select.clicked.connect(self.fileselect)
        self.file_select.clicked.connect(self.fileselect)


    def CalculateOutput(self):
        try:
            with open(self.filename, 'r') as fp: #open data file
                reader = csv.reader(fp, delimiter=',', quotechar='"')
                devicelist = []
                xylist = []
                templist = []
                for row in reader:  #build 3 lists: devices, x,y coordinates, and temperatures
                        devicelist.append(row[0])
                        xylist.append((row[1],row[2]))
                        templist.append(row[3])

                del devicelist[0], xylist[0],templist[0]    #delete headers

                myxnumber = str(self.x_value_input.toPlainText())   #grab input value for x

                myynumber = str(self.y_value_input.toPlainText()) #grab input value for y

                some_pt = (myxnumber, myynumber) #create user selected point x,y

                calc = xylist[distance.cdist([some_pt], xylist).argmin()] #calculate closest x,y coordinate

                closesttemp = templist[xylist.index(calc)] #return corresponding temperature per closest x,y coordinate

                closestdevice = devicelist[xylist.index(calc)] #return corresponding device per closest x,y coordiante

                returnstring = 'The temperature is: ' + str(closesttemp) + ' for the closest x,y coordinate: ' + str(calc) + ' which is device: ' + str(closestdevice)

                self.results_window.setText(returnstring)
        except:
            self.results_window.setText('Not a FDS exported .csv file or no x,y coordinate entered')

    def fileselect(self): #select file, returns path
        fname, _ = QtWidgets.QFileDialog.getOpenFileName()
        self.filename = fname
        self.success_fail.setText('Loaded')
        return(fname)

if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    dialog = QtWidgets.QMainWindow()
    prog = FDSApp(dialog)
    dialog.show()
    exit(app.exec_())
