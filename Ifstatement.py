import TransferFunction

class Ifstatement:
    @staticmethod
    def hurwitz_stability_check(data):
        if data["a1"] * data["a2"] > data["a3"] * data["a0"]:               #Stabliny
            return 1
        if data["a1"] * data["a2"] == data["a3"] * data["a0"]:
            return 0                                                        #Granica stabilności
        return -1                                                           #Niestabilny

    @staticmethod
    def routh_stability_check(data):
        if data['a3'] > 0 and data['a2'] > 0 and data['a1'] > 0 and data['a0'] > 0:
            return True
        return False
    @staticmethod
    def is_integer(value):
        if isinstance(value, int):
            return True
        return False








