class Person:
    
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
        self.studentId=studentId
    
    def showStudentInfo(self):
        print(f" Student Id is  :{self.studentId}")
        self._showPersonInfo()
        print(f"FullName Length is : {self._getFullName()}")
#=============================================================        
        
# class Teacher(Person):
#     def __init__(self, name, family, age,TeachertId):
#         super().__init__(name, family, age)    
#         self.__TeachertId=TeachertId
    
#     def showTeacherInfo(self): 
#         print(f" Teacher  Id is  :{self.TeachertId}")
#         self.__showPersonInfo()
#         print(f"FullName Length is : {self._getFullName}")        
           
        
# s1=Person("Jack","Jackson",25)        
# s1.showPersonInfo()
# print("==============================")
t1=Student("Mike","Trump",45,500)        
t1.showStudentInfo()
        