class Deduction:
    def __init__(self, description, date, charge, empID):
        self.__description = description
        self.__date = date
        self.__charge = charge
        self.__empID = empID

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_charge(self):
        return self.__charge
    
    def get_empID(self):
        return self.__empID