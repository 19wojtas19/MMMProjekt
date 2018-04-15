import TransferFunction

class Ifstatement:
    @staticmethod
    def hurwitz_stability_check(self, data):
        if data["a1"] * data["a2"] > data["a3"] * data["a0"]:               #Stabliny
            return 1
        if data["a1"] * data["a2"] == data["a3"] * data["a0"]:
            return 0
        return -1

    @staticmethod
    def routh_stability_check(self, object):
        char_eq = object.get_data()
        if char_eq["a3"] > 0 and char_eq["a2"] > 0 and char_eq["a1"] > 0 and char_eq["a0"] > 0:
            return True
        return False



