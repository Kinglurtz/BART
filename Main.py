import BartMainGUI as GUI
import os
from Util import Drink
from Util import Pump
from Util import Util
from PyQt5 import QtCore, QtGui, QtWidgets

def main():

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bart = QtWidgets.QWidget()
    ui = GUI.Ui_Bart()
    ui.setupUi(Bart)
    
    #Load the pump and drink config files
    pumpList = Util.LoadPumpConfig()
    drinkList = Util.LoadDrinkConfig()
    #Validate pump numbers for ingredients
    for drink in drinkList:
      drink.VerifyIngredientsInStock(pumpList)
    #Set up events for each stacked widget settings/2/3/4 pumps
    ui.SetUpSettingsPageEvents()
    ui.SetUp2SliderPageEvents(pumpList, drinkList)
    ui.SetUp3SliderPageEvents(pumpList, drinkList)
    ui.SetUp4SliderPageEvents(pumpList, drinkList)
    #TODO verify the pumps and drinks match ingredients
    ui.SetDrinkImages(drinkList)
    ui.SetDrinkPages(drinkList)
    

    
    Bart.showFullScreen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()