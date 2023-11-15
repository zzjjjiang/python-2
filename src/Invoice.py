class Invoice:
    # def __init__(self, arguments):
    #     self.__invoice_id = int(arguments[0])
    #     self.__user_id = int(arguments[1])
    #     self.__amount = float(arguments[2])
    #     self.__paid = arguments[3]=='True'
    
    def __init__(self, invoice_id, user_id, amount, paid):
        self.__invoice_id = int(invoice_id)
        self.__user_id = int(user_id)
        self.__amount = float(amount)
        self.__paid = str(paid)=='True'
    
    def __repr__(self):
        return f"Invoice(invoice_id='{self.__invoice_id}', user_id='{self.__user_id}', amount='{self.__amount}', paid='{self.__paid}')"