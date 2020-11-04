import sys
import os
import numpy as np

def input_error():
    print('Invalid input. Press any key to try again.')
    take = input()

## BASE CHARACTER
class Character():
    def __init__(self, name, race, class1, hp, ac, stre, dex, con, intel, wis, char):
        self.name = name
        self.race = race
        self.class1 = int(class1)
        self.hp = int(hp)
        self.ac = int(ac)
        self.stre = int(stre)
        self.dex = int(dex)
        self.con = int(con)
        self.intel = int(intel)
        self.wis = int(wis)
        self.char = int(char)
        #modifiers
        self.modhp = hp -10
        self.modstre = stre -10
        self.moddex = dex -10
        self.modcon = con -10
        self.modintel = intel -10
        self.modwis = wis -10
        self.char = char -10
        self.ini = self.moddex
        self.backstory = None
        self.alignment = None
        self.faith = None 
        self.gp = None
        self.hair = None
        self.skin = None
        self.eyes = None
        self.height = None
        self.weight = None
        self.age = None
        self.gender = None
        self.traits = []
        self.ideals = []
        self.bonds = []
        self.flaws = []
    def backstory_creation(self):
        backstory = input("Give a backstory for " + self.name + "\n> ")
        self.backstory = backstory
    def character_details(self):
        def alignment_selection(self):
            alignment = input('Choose Alignment \n> ').lower()
            if alignment != 'ce' or 'cg' or 'cn' or 'le' or 'lg' or 'ln' or 'ne' or 'ng' or 'n':
                self.alignment = alignment.upper()
            else: 
                input_error()
                alignment_selection(self)
        
        def faith_selection(self):
            faith = input('Faith: \n>')
            self.faith = faith

        def physic_selection(self):

            traits_input = input('List some traits, seperate with commas: \n> ')
            self.traits = traits_input.split(',')

            ideals_input = input('List some ideals, seperate with commas: \n> ')
            self.ideals = ideals_input.split(',')

            bonds_input = input('List some bonds, seperate with commas: \n> ')
            self.bonds = bonds_input.split(',')

            flaws_input = input('List some flaws, seperate with commas: \n> ')
            self.flaws = flaws_input.split(',')
