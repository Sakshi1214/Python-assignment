# class creation
from abc import ABC, abstractmethod
class Person(ABC):
    @abstractmethod
  
   

    def get_gender(self):
        pass
        
        
class male(Person):
           def get_gender(self):
             print(male)
class female(Person):
        def get_gender(self):
          print(female)

# class instantiation
try:
    person = Person()
    print(person.get_gender())
except TypeError as e:
    print("Error:",e)
