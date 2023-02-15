from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        raise NotImplementedError
    @abstractmethod
    def sleep(self):
        raise NotImplementedError
class Dog(Animal):
    def sound(self):
        print ('Ham Ham!')
    def sleep(self):
        print('ZZZZ')
class Cat(Animal):
    def sound(self):
        print('Miau Miau!')
    def sleep(self):
        print('prrr')

dog=Dog()
dog.sound()

cat=Cat()
cat.sleep()