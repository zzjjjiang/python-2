class Calculator:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2
        self.__result=None
    
    def add(self):
        self.__result=self.__num1+self.__num2
        
    def sub(self):
        self.__result=self.__num1-self.__num2
        
    def mul(self):
        self.__result=self.__num1*self.__num2
        
    def div(self):
        if self.__num2 == 0:
            raise ValueError('cannot divide by 0')
        else:
            self.__result=self.__num1/self.__num2
            
    def get_result(self):
        return self.__result 