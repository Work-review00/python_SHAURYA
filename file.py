"""import my_module

chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

index = my_module.find_index(chicks, 'emo')
print(index)"""

"""import my_module as mm #imported as mm

chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

index = mm.find_index(chicks, 'emo')
print(index)"""

"""from  my_module import  find_index #function directly imported
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

index = find_index(chicks, 'emo')
print(index)"""
"""
from  my_module import  find_index, test #to import other things 
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

index = find_index(chicks, 'emo')
print(index)
print(test)"""


"""from  my_module import  find_index as fi, test #to import as a name
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

index = fi(chicks, 'emo')
print(index)
print(test) """

"""from  my_module import * #to import everything directly but confusion arises as what got imported  
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

index = find_index(chicks, 'emo')
print(index)
print(test) """

"""from  my_module import  find_index, test #to import other things 
import sys # to find path
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

index = find_index(chicks, 'emo')
print(sys.path)"""

"""import random #random module
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

random_chick= random.choice(chicks)
print(random_chick)"""

"""import math #for mathematical operations
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

rads = math.radians(60)
print(rads)
print(math.sin(rads))"""

"""import datetime #for date and time operations
import calendar #for calendar things
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

today = datetime.date.today()
print(today)
print(calendar.isleap(2024))"""

import os # os info and access to files 
print(os.getcwd()) #location of directory
print(os.__file__) # location of file 