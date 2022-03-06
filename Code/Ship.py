from Vehicle import Vehicle
# Ship class is a child of Vehicle class
class Ship(Vehicle):
    # atribut private
    __age = 0                   # usia/tahun
    __type = ""
    __countryOfManufacture = ""

    # contructor
    def __init__(self):
        super().__init__()
        self.__age = 0
        self.__type = ""
        self.__countryOfManufacture = ""
    
    # setter
    def setAge(self, age):
        self.__age = age
    def setType(self, type):
        self.__type = type
    def setCountryOfManufacture(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture
    
    # getter
    def getAge(self):
        return self.__age
    def getType(self):
        return self.__type
    def getCountryOfManufacture(self):
        return self.__countryOfManufacture
    
    # print method
    def printShip(self):
        self.printVehicle()
        print("Age                    : " + str(self.getAge()) + " Years")
        print("Type                   : " + self.getType())
        print("Country Of Manufacture : " + self.getCountryOfManufacture())
        self.move("Not Move")
        print("______________________________________________")