# file objects 

'''f = open('text.txt', encoding='utf-8')

print(f.read())

f.close()''' 

#using context managers 

'''with open('text.txt', encoding='utf-8') as f:  #f represents the opened file
    print(f.read())   #gets closed automatically

print("Done")
print(f.closed)
print(f.read())'''

'''with open('text.txt', 'r', encoding= 'utf-8') as f:
    f_contents = f.read()
    print(f_contents)'''

'''with open('text.txt', 'r', encoding= 'utf-8') as f:
    f_contents = f.readlines ()
    print(f_contents)'''

'''with open('text.txt', 'r', encoding= 'utf-8') as f:
    f_contents = f.readline() #for single line and this will automatically fetch the lines in the order
    print(f_contents)'''

'''with open('text.txt', 'r', encoding= 'utf-8') as f:
    f_contents = f.readline() #for single line and this will automatically fetch the lines in the order
    print(f_contents, end='') '''#will not give a new line space

'''with open('text.txt', 'r', encoding= 'utf-8') as f:

    for line in f:
        print(line, end = '') '''#to print out all of the lines in the file 


'''with open('text.txt', 'r', encoding= 'utf-8') as f:
    f_contents = f.read(100) # to read lines till the mentioned size ..as the character
    print(f_contents, end='') '''


##Iterating through small chunks for a large file: 


'''with open('text.txt', 'r', encoding= 'utf-8') as f:

    size_to_read = 100

    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
          print(f_contents, end= '')
          f_contents = f.read(size_to_read)'''

'''with open('text.txt', 'r', encoding= 'utf-8') as f:

    size_to_read = 10

    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
          print(f_contents, end= '*') #* at every 10th character
          f_contents = f.read(size_to_read)'''

'''with open('text.txt', 'r', encoding= 'utf-8') as f:

    size_to_read = 10

    f_contents = f.read(size_to_read)

    print(f.tell())'''


'''with open('text.txt', 'r', encoding= 'utf-8') as f:

    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents, end= '')

    f_contents = f.read(size_to_read)
    print(f_contents, end= '')'''

'''with open('text.txt', 'r', encoding= 'utf-8') as f:

    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents, end= '')

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents, end= '')
    '''

'''with open('test.txt','w') as f:
    pass'''

'''with open('test.txt','w') as f:
     f.write('test')
     f.write('test') '''

'''with open('test.txt','w') as f:
     f.write('test')

     f.seek(0) #would overwrite the first argument

     f.write('test')'''

'''with open('test.txt','w') as f:
     f.write('test')

     f.seek(0) 
     
     f.write('D') '''#could be confusing as here only the first letter is getting replaced 

'''with open('text.txt', 'r', encoding= 'utf-8') as rf:
    with open('test.txt', 'w', encoding='utf-8')as wf:
        for line in rf:
            wf.write(line)   #to write contents of a file in a new file'''

'''with open(r'C:\\Users\\patha\\Downloads\\Untitled design (1).png', 'rb') as rf:
    with open('Untitled design_copy (1).png', 'wb')as wf:   #rb and wb as for binary code as for the images
        for line in rf:
            wf.write(line)'''


'''with open(r'C:\\Users\\patha\\Downloads\\Untitled design (1).png', 'rb') as rf:
    with open('Untitled design_copy (1).png', 'wb')as wf:   #rb and wb as for binary code as for the images
        for line in rf:
            wf.write(line)'''


with open(r'C:\Users\patha\Downloads\Untitled design (1).png', 'rb') as rf:
    with open('Untitled design_co2py (1).png', 'wb')as wf:   #rb and wb as for binary code as for the images
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)