import os
import threading
from Util import Drink
from Util import Pump

def LoadPumpConfig():

    fileDir = os.path.dirname(__file__)
    pumpList = []
    with open(os.path.join(fileDir, "../Docs/PumpConfig.txt")) as f:
        for idx,line in enumerate(f):
            pumpList.append(Pump.Pump(idx, line))

    return pumpList

def LoadDrinkConfig():

    fileDir = os.path.dirname(__file__)
    drinkList = []
    with open(os.path.join(fileDir, "../Docs/DrinkConfig.txt")) as f:
        for line in f:
            drinkList.append(Drink.Drink(line))
    return drinkList

def Brew(drink, pumpList):
    print("Brewing your drink: " + drink.name)
    totalML = 0
    FLOW_RATE = Pump.FLOW_RATE
    threadList = []
    for i in drink.ingredients:
        print(i)
        totalML += i.volume
    print("Total ml: " + str(totalML))
    for i in drink.ingredients:
        thread = threading.Thread(target=pumpList[i.pumpNumber].Pour, args=([float(i.volume) * FLOW_RATE]))
        threadList.append(thread)
    for thread in threadList:
        thread.start()
    for thread in threadList:
        thread.join()
    print("Drink ready")
