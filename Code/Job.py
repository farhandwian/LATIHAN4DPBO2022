# The Job class is the parent of the Driver class
class Job:
    # Private atribut
    __nip = ""
    __companyName = ""
    __position = ""

    # constructor
    def __init__(self):
        self.__nip = ""
        self.__companyName = ""
        self.__position = ""
    
    # setter getter
    def setNip(self, nip):
        self.__nip = nip
    def setCompanyName(self, companyName):
        self.__companyName = companyName
    def setposition(self,position):
        self.__position = position
 
    def getNip(self):
        return self.__nip
    def getCompanyName(self):
        return self.__companyName
    def getPosition(self):
        return self.__position

    # print method
    def printJob(self):
        print("NIP           : " + self.getNip())
        print("Company Name  : " + self.getCompanyName())
        print("Position      : " + self.getPosition())