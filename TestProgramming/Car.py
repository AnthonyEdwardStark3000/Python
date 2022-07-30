class car:
    def __init__(self, carId="0", modelNumber="0",
                 colour="red", transmissionType="petrol", fuelType="petrol", engineType="volvo", bodyType="metal",
                 engineDisplacement=12, bootSpace=4, seatCapacity=6

                 ):
        self.seatCapacity = seatCapacity
        self.bootSpace = bootSpace
        self.engineDisplacement = engineDisplacement
        self.bodyType = bodyType
        self.fuelType = fuelType
        self.transmissionType = transmissionType
        self.colour = colour
        self.carId = carId
        self.modelNumber = modelNumber
        self.engineType = engineType

        #Getter
    def get_seatCapacity(self):
        return self._seatCapacity

    def get_bootSpace(self):
        return self._bootSpace

    def get_engineDisplacement(self):
        return self._engineDisplacement

    def get_bodyType(self):
        return self._bodyType

    def get_fuelType(self):
        return self._fuelType

    def get_transmissionType(self):
        return self._transmissionType

    def get_colour(self):
        return self._colour

    def get_carId(self):
        return self._carId

    def get_modelNumber(self):
        return self._modelNumber

    def get_engineType(self):
        return self._engineType

    #Setter

    def set_seatCapacity(self, seat):
        self._seatCapacity = seat

    def set_bootSpace(self, boot):
        self._bootSpace = boot

    def set_engineDisplacement(self, engine):
        self._engineDisplacement = engine

    def set_bodyType(self, body):
        self._bodyType = body

    def set_fuelType(self, fuel):
        self._fuelType = fuel

    def set_transmissionType(self, transmission):
        self._transmissionType = transmission

    def set_colour(self, color):
        self._colour = color

    def set_carId(self, id):
        self._carId = id

    def set_modelNumber(self, modelnum):
        self._modelNumber = modelnum

    def set_engineType(self, enginetype):
        self._engineType = enginetype


    def createCarDetails(self):
       count = int(input("Enter the number of car details to created\n"))

       for i in range(count):
           id = input("Enter Car Id")
           model = input("Enter Model Number")
           color = input("Enter Colour")
           transmission = input("Enter Transmission Type")
           fuel = input("Enter Fuel Type")
           engine = input("Enter Engine Type")
           body = input("Enter Body Type")
           displacement = int(input("Enter Engine Displacement"))
           space = int(input("Enter Boot Space"))
           seat = int(input("Enter Seat Capacity"))

# self._year = a
c = car()
c.createCarDetails()

