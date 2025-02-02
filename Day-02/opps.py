
#opps modeule
#object class in python


class Employee(object):
    #constructor (basically this is the desin, means attributes)
    def __init__(self,empno,ename,sal=500):
        self.eno=empno #instance variables/properties
        self.name=ename 
        self.salary=sal
        self.bonus=10000
        self.__variable=20000

    # def __init_subclass__(cls):
    #     pass

    def ShowDetails(self): #Methed
        #check difference between Method and function
        print('Eno',self.eno)
        print('Ename',self.name)
        print('EPay',self.salary)
        print('Total_pay', self.salary+self.bonus)
        print('Total', self.salary+self.bonus+self.__variable)


if __name__ == '__main__':
    s1=Employee(101,'Pramod',88888)
    s1.ShowDetails()
    s1.bonus=500000
    print(s1.bonus)
    #print(s1.__variable())