from Driver import Driver
from Ship import Ship
from Airplane import Airplane

def main():
    nik = ["1901", "2302", "4703"]
    nama = ["Ahmad rusydi", "azar muslimin", "ingwer jeremias"]
    gender = ["Male", "Male", "Male"]
    
    nip = ["9101", "9102", "9103"]
    perusahaan = ["FOrd", "Redix", "Samantha"]
    posisi = ["CEO", "CEO", "President"]
    
    sim = ["1201029", "3602169", "6403869"]
    masaAktif = ["3012", "3015", "3012"]
    tipeKendaraan = ["Sport racing", "Moge", "kolbak"]

    oDriver = [Driver() for i in range(3)]

    # enter driver data
    for i in range(3):
        oDriver[i].setNik(nik[i])
        oDriver[i].setName(nama[i])
        oDriver[i].setGender(gender[i])
        oDriver[i].setNip(nip[i])
        oDriver[i].setCompanyName(perusahaan[i])
        oDriver[i].setposition(posisi[i])
        oDriver[i].setLicenseID(sim[i])
        oDriver[i].setActiveUntil(masaAktif[i])
        oDriver[i].setVehicleType(tipeKendaraan[i])

    # print driver information
    print("+++++++++++++++++++++++++++++++++++")
    print("            Driver Data            ")
    print("+++++++++++++++++++++++++++++++++++\n")
    for i in range(3):
        oDriver[i].printDriver()

    # data for ship class 
    nameS = ["KM Kambuna", "Princess Irene", "KFC Mahakam"]
    fuelS = ["Oil", "Oil","Deuterium"]
    penumpangS = [5818, 1212, 8181]
    usiaS = [11, 12, 10]
    tipeS = ["Battleships", "Battleships", "Battleships"]
    produksiS = ["Indonesia", "Indonesia", "Germany"]

    oShip = [Ship() for i in range(3)]
    # enter ship data
    for i in range(3):
        oShip[i].setName(nameS[i])
        oShip[i].setFuelType(fuelS[i])
        oShip[i].setMaxPassanger(penumpangS[i])
        oShip[i].setAge(usiaS[i])
        oShip[i].setType(tipeS[i])
        oShip[i].setCountryOfManufacture(produksiS[i])

    # print data Ship nya
    print("\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++")
    print("               Ship Information               ")
    print("++++++++++++++++++++++++++++++++++++++++++++++\n")
    for i in range(3):
        oShip[i].printShip()

    
    # data for Airplane class
    nameA = ["Boeing 747", " F-35 Lightning II. Raptor", "Shenyang FC-31 B-2 Spirit"]
    fuelA = ["Kerosene", "Kerosene", "Kerosene"]
    penumpangA = [467, 1, 2]
    usiaA = [13, 8, 18]
    tipeA = ["War Aircraft", "War Aircraft", "War Aircraft"]
    panjangSayapA = [20, 20, 20]

    
    oAirplane = [Airplane() for i in range(3)]
    # enter airplane data
    for i in range(3):
        oAirplane[i].setName(nameA[i])
        oAirplane[i].setFuelType(fuelA[i])
        oAirplane[i].setMaxPassanger(penumpangA[i])
        oAirplane[i].setAge(usiaA[i])
        oAirplane[i].setType(tipeA[i])
        oAirplane[i].setWingsLength(panjangSayapA[i])

    # print 
    print("\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++")
    print("             Airplane information             ")
    print("++++++++++++++++++++++++++++++++++++++++++++++\n")
    for i in range(3):
        oAirplane[i].printAirplane()
    

if __name__=="__main__":
    main()