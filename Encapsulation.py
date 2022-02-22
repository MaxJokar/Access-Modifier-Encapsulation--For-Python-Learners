class Person:
    __x=None #Private varible ,is used in here ONLY
    __y=None #Public varaible is used in children 
    z=None  #be accessed by all func,instance etc
    
    def __init__(self,name, family, age):
        self.__name=name
        self.__family=family
        self.__age=age
        
    def _showPersonInfo(self):
        print(f" Name:{self.__name}")
        print(f" Family:{self.__family}") 
        print(f" Age:{self.__age}")  
        
    def _getFullName(self):
        return len(self.__name)+len(self.__family)       
#======CHILDREN CAN ACCESS TO PROTECTED FIELDS  LIKE:showPersonInfo by Adding " _"===============================================    
class Student(Person):
    def __init__(self, name, family, age,studentId):
        super().__init__(name, family, age)    
        self.__studentId=studentId
    
    def showStudentInfo(self):
        print(f" Student Id is  :{self.__studentId}")
        self._showPersonInfo()
        print(f"FullName Length is : {self._getFullName()}")
        self._y=1000
        self.z=2000
        print (f" VaribleS Are accessed : {self._y}: {self.z}")
#=============================================================        
        
class Teacher(Person):
    def __init__(self, name, family, age,TeachertId):
        super().__init__(name, family, age)     
        self.__TeachertId=TeachertId
    
    def showTeacherInfo(self): 
        print(f" Teacher  Id is  :{self.__TeachertId}")
        self._showPersonInfo()
        print(f"FullName Length is : {self._getFullName()}")  
        self._y=2
        self.z=5
        print (f" VaribleS Are accessed : {self._y}: {self.z}")      
           
#usual instance CAN NOT ACCESS TO THE  PRIVATE fileds:       
# s1=Person("Jack","Jackson",25)        
# s1.showPersonInfo()
# print("==============Student Data================")
t1=Student("Mike","Trump",45,500)        
t1.showStudentInfo()

print("============Teacher Data==================")
t1=Teacher("Maxxx","Clinton",415,5800)        
t1.showTeacherInfo()  