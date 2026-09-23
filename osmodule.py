'''import os 
#print(dir(os)) #shows all attributes and methods we have access to in this module
#print(os.getcwd())
#os.chdir() #used to change directory
#print(os.listdir()) #list of files and folders in the current directory

#os.mkdir()  #used to create a new directory 
#os.makedirs('ye_da_goat') #used to create a new directory but it works deep 
#os.rmdir() #to remove directory 
#os.removedirs('ye_da_goat') 
#os.mkdir('test.txt')
# os.rename('test.txt', 'demo.txt')
# print(os.stat('demo.txt'))
#print(os.stat('demo.txt').st_size)  
#print(os.stat('demo.txt').st_mtime)  

from datetime import datetime
mod_time = (os.stat('demo.txt').st_mtime) 
print(datetime.fromtimestamp(mod_time))''' 

#import os 
'''for dirpath, dirnames, filenames in os.walk(r 'F:\\pythondev\\demo.txt'): #to see the directory tree
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()'''


#print(os.environ)
'''for key, value in os.environ.items():
    print(key, '=', value)'''

#print(os.environ.get('VIRATV'))
'''import os

#print(os.environ.get('USERPROFILE'))

'test.txt'

#file_path = os.environ.get('USERPROFILE') + 'test.txt'  #faulty method
file_path = os.path.join(os.environ.get('USERPROFILE') , 'test.txt' )
print(file_path)
'''

#import os
'''
print(os.path.basename('/tmp/text.txt'))
print(os.path.dirname('/tmp/text.txt'))
print(os.path.split('/tmp/text.txt'))
print(os.path.exists('/tmp/text.txt'))
print(os.path.isdir('/tmp/text.txt'))
print(os.path.isfile('/tmp/text.txt'))
print(os.path.splitext('/tmp/text.txt'))
'''

#print(dir(os.path))