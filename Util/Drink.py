import os
"""
The Drink class is created following a CSV format. The below is the template for the file. 

[Name of drink],[Image File(from Images folder)], [Number of ingredients], [Ingredient 1 name], [Ingredient 1 quantity(in ml)], ...

The CSV file for the drinks is located in the DOC directory. File Name: DrinkConfig.txt

"""

class Drink:

    def __init__(self, line):
        input = [x.strip() for x in line.split(',')]
        self.name = input[0] #Get Name
        self.imagePath = os.path.dirname(__file__) + "/../Images/" + input[1] #Build image path
        #TODO Add a valid image path checker.
        self.ingredientCount = int(input[2]) #Getting count of ingredients
        self.ingredients = []
        for i in range(0, self.ingredientCount):
            self.ingredients.append(Ingredient(input[i * 2 + 3], input[i * 2 + 4]))

    def VerifyIngredientsInStock(self, pumpList):
        for i in self.ingredients:
            i.GetPumpNumber(pumpList)
            if i.pumpNumber == -1:
                print("Ingredient was not on tap")
                #Maybe remove Drink from list??? or something idk

    def __str__(self):
        return "Drink: " + self.name
            

        
        
class Ingredient:
    
    def __init__(self, name, volume):
        self.name = name
        self.pumpNumber = -1
        self.volume = int(volume)

    def __str__(self):
        return "Ingredient - " + self.name + ": " + str(self.volume) + "ml"

    def GetPumpNumber(self, pumpList):
        for pump in pumpList:
            if self.name == pump.ingredient:
                self.pumpNumber = pump.pumpNumber
                return