'''import csv

html_output = ''
names = []

with open ('newfile.csv', 'r') as data_file:
    csv_data = csv.reader (data_file)

   # print(csv_data)   # will give the csv reader object 
  #  print(list(csv_data))  #will give the list but would be messy 

    next(csv_data)  #will skip the first line
    next(csv_data)    #will skip the second line 

    for line in csv_data:
        #print(line) #to print every line
        names.append(f"{line[0]} {line[1]}")

for name in names:
    print(name)'''



'''import csv

html_output = ''
names = []

with open ('newfile.csv', 'r') as data_file:
    csv_data = csv.reader (data_file) 

    next(csv_data)  
    next(csv_data)    

    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}")


for name in names:
    print(name)
'''


'''
import csv

html_output = ''
names = []

with open ('newfile.csv', 'r') as data_file:
    csv_data = csv.reader (data_file) 

    next(csv_data)  
    next(csv_data)    

    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}")


html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'


html_output += '\n</ul>'

print(html_output)
'''



import csv

html_output = ''
names = []

with open ('newfile.csv', 'r') as data_file:
    csv_data = csv.DictReader (data_file) 

    next(csv_data)    
    
    for line in csv_data:
        if line['FirstName'] == 'No Reward':
                break
        names.append(f"{line['FirstName']} {line['LastName']}")
    
html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'


html_output += '\n</ul>'

print(html_output)
    
