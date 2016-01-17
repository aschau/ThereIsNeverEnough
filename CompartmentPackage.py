from Compartment import *

class CompartmentPackage:
    def __init__(self, compType, xy):
        self.type = compType
        self.GUI = None #DrawObject
        self.compartment = Compartment()

    def typeWeapon(self):
        pass

    def update(self, selected):
        self.compartment.update()

    def draw(self):
        self.GUI.draw(self.compartment.selected, not self.compartment.active)
    
    # Getters
    def selected(self):
        return self.compartment.selected
    def active(self):
        return self.compartment.active

    # Setters
    def select(self):
        self.compartment.select()
    def deselect(self):
        self.compartment.deselect()
