class TaxMan:
    def __init__(self, lst, percent):
        self.__lst = lst
        self.__percent = float(percent[:-1])
        self.__totalTax = 0.0
        
    def calc_total(self):
        self.__totalTax = round(sum(map(lambda i : i['price'] * (1 + self.__percent/100), self.__lst)), 2)
        
    def get_total(self):
        return self.__totalTax