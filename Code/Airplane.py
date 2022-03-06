from Vehicle import Vehicle
# airplane class is child of vehicle class
class Airplane(Vehicle):
    # private atribut 
    __age = 0           
    __type = ""
    __wingsLength = 0   

    # contructor
    def __init__(self):
        super().__init__()
        self.__age = 0
        self.__type = ""
        self.__wingsLength = 0
    
    # setter
    def setAge(self, age):
        self.__age = age
    def setType(self, type):
        self.__type = type
    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength
    
    # getter 
    def getAge(self):
        return self.__age
    def getType(self):
        return self.__type
    def getWingsLength(self):
        return self.__wingsLength
    
    # print
    def printAirplane(self):
        self.printVehicle()
        print("Age                    : " + str(self.getAge()) + " Years")
        print("Type                   : " + self.getType())
        print("Wings Length           : " + str(self.getWingsLength()) + " Meters")
        self.move("Move")
        print("______________________________________________")