import random

class SmartFanaria():

    def __init__(self, name):
        self.amaountOfCars = random.randint(0,50)
        self.name = name

    def greenLight(self):
        
        self.x = random.randint(5,10) #posa amaksia feugoun otan ginete prasino to fanari

        if self.amaountOfCars<10: #epidi mpori na exi 10 amaksia to fanari, den 8a mporoun na figoun apo 5-10 pi8anos
            self.x = 1
            self.count = 0
            self.temp = self.amaountOfCars
            while self.amaountOfCars>0 :
                self.amaountOfCars = self.amaountOfCars - self.x
                self.count = self.count + 1
            self.carsOut = self.count
            print("To ",self.name, " ine prasino kai exi " , self.temp, " amaksia kai feugoun ", self.carsOut )
        else :
            self.carsOut = self.x
            print("To ",self.name, " ine prasino kai exi " , self.amaountOfCars, " amaksia kai feugoun ", self.carsOut )        
            self.amaountOfCars = self.amaountOfCars - self.x

    def redLight(self):
        
        self.carsIn = random.randint(0,5)
        print("To ",self.name, " ine kokino kai exi " , self.amaountOfCars, " amaksia kai erxonte " , self.carsIn)
        self.amaountOfCars = self.amaountOfCars + self.carsIn

# Main

fanari1 = SmartFanaria("A")
fanari2 = SmartFanaria("B")
fanari3 = SmartFanaria("C")

while fanari1.amaountOfCars!=0 or fanari2.amaountOfCars!=0 or fanari3.amaountOfCars!=0: # To programa telioni otan den exoun amaksia ta fanaria
    if fanari1.amaountOfCars > fanari2.amaountOfCars and fanari1.amaountOfCars > fanari3.amaountOfCars:
        fanari1.greenLight()
        fanari2.redLight()
        fanari3.redLight()
    elif fanari2.amaountOfCars > fanari1.amaountOfCars and fanari2.amaountOfCars > fanari3.amaountOfCars :
        fanari2.greenLight()
        fanari1.redLight()
        fanari3.redLight()
    elif fanari3.amaountOfCars > fanari1.amaountOfCars and fanari3.amaountOfCars > fanari2.amaountOfCars :
        fanari3.greenLight()
        fanari1.redLight()
        fanari2.redLight()
    else : #h periptosi pou ine isa
        fanaria = [fanari1 , fanari2 , fanari3]
        temp = random.choice(fanaria) #kratao ena tixeo fanari se periptosi pou ta amaksia tous ine isa
        fanaria.remove(temp) #bgazo apo tin lista to temp
        
        temp.greenLight()
        fanaria[0].redLight()
        fanaria[1].redLight()

print(fanari1.amaountOfCars , " A")
print(fanari2.amaountOfCars , " B")
print(fanari3.amaountOfCars , " C")