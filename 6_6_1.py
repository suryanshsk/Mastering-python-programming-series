"""considered a blueprint for other classes.
It allows you to create a set of methods that
 must be created within any child classes built
   from the abstract class"""
from abc import ABC, abstractmethod

# Abstract Class: Song
class Song(ABC):
    @abstractmethod
    def perform(self):
        pass  # Defines the rhythm

# Dancer 1
class Dancer1(Song):
    def perform(self):
        return "Dancer 1 adds smiles to the rhythm!"

# Dancer 2
class Dancer2(Song):
    def perform(self):
        return "Dancer 2 adds unique moves to the rhythm!"

# Test the dancers
print(Dancer1().perform())
print(Dancer2().perform())

