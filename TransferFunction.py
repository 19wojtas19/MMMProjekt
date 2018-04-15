class TransferFunction:
    template = ["b0", "a3","a2","a1","a0"]
    data = None
    def value_check(self):
        for value in self.template:
            if value not in self.data.keys():
                print("missing parameters from input")
                return False
        return True

    def get_data(self):
        return self.data

    def __init__(self, data):
        if data is not None:
            self.data = data
            self.value_check()
