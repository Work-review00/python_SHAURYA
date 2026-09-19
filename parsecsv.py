'''import csv

with open ('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

   # print(csv_reader) #gives csv object

    #next(csv_reader) # will skip the first element in this case email

    with open('new_names.csv', 'w') as new_file:
         csv_writer = csv.writer(new_file, delimeter = '-')  

    for line in csv_reader:
        #print(line) # prints each line from the csv file in form of a list 
        print(line[2]) # will print the element over 2nd index in this case email of every name '''


'''import csv

with open ('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)


    with open('new_names.csv', 'w') as new_file:
             #csv_writer = csv.writer(new_file, delimiter = '-')   #separating values using -
             csv_writer = csv.writer(new_file, delimiter = '\t')   #separating values using tabs


             for line in csv_reader:
                    csv_writer.writerow(line)'''


'''import csv

with open ('new_names.csv', 'r') as csv_file:     
    #csv_reader = csv.reader(csv_file)       #delimiter not passed so no commas and space ..came as one whole value
    csv_reader = csv.reader(csv_file, delimiter = '\t')   #now delimiter passed so comma will be there 

    for line in csv_reader:
            print(line)


    with open('new_names.csv', 'w') as new_file:
             #csv_writer = csv.writer(new_file, delimiter = '-')   #separating values using -
             csv_writer = csv.writer(new_file, delimiter = '\t')   #separating values using tabs


             for line in csv_reader:
                    csv_writer.writerow(line)'''



'''import csv

with open ('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)  #transform the field names as keys of the value ..and makes a dictionary makes easir to parse

    for line in csv_reader:
        print(line)
'''

'''import csv

with open ('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)  #transform the field names as keys of the value ..and makes a dictionary makes easir to parse

    for line in csv_reader:
        print(line['email'])'''


'''import csv

with open ('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)  


    with open('new_names.csv', 'w') as new_file:
                 fieldnames = ['first_name','last_name', 'email']
                 csv_writer = csv.DictWriter(new_file, fieldnames= fieldnames, delimiter = '\t')   #separating values using tabs

                 csv_writer.writeheader()
    
                 for line in csv_reader:
                        csv_writer.writerow(line)'''


import csv

with open ('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)  


    with open('new_names.csv', 'w') as new_file:
                 fieldnames = ['first_name','last_name']   #removed email
                 csv_writer = csv.DictWriter(new_file, fieldnames= fieldnames, delimiter = '\t')   #separating values using tabs

                 csv_writer.writeheader()
    
                 for line in csv_reader:
                        del line['email']   # deleted email of each line 
                        csv_writer.writerow(line)


    
            
