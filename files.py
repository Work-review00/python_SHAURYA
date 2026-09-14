'''import os

os.chdir('C:\\Users\\patha\\Desktop\\ikgptu')

print(os.getcwd())'''

'''import os

os.chdir('C:\\Users\\patha\\Desktop\\ikgptu')

for f in os.listdir():
    print(f)'''

'''import os

os.chdir('C:\\Users\\patha\\Desktop\\ikgptu')

for f in os.listdir():
    print(os.path.splitext(f))   '''#gives tuple of file name and the extension



'''import os

os.chdir('C:\\Users\\patha\\Desktop\\ikgptu')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(f'Original: {f}')
    print(f'Name: {file_name}')
    print(f'Extension: {file_ext}')
    print('---')'''

'''import os

os.chdir('C:\\Users\\patha\\Desktop\\ikgptu')

for f in os.listdir():
    file_name, file_ext= os.path.splitext(f) 
    print(file_name)'''


'''import os

os.chdir('C:\\Users\\patha\\Desktop\\ikgptu')

for f in os.listdir():
    f_name, f_ext= os.path.splitext(f) 
    f_title, f_course, f_number = f_name.split('-')
    print('{}-{}-{}{}'.format(f_number, f_course, f_title, f_ext))'''


'''import os
os.chdir('C:\\Users\\patha\\Desktop\\ikgptu')

for f in os.listdir():
    f_name, f_ext= os.path.splitext(f) 
    f_title, f_course, f_number = f_name.split('-')

    f_title = f_title.strip()  #would remove the space
    f_course = f_course.strip()  #would remove the space
    f_number = f_number.strip() #would remove the space
    # f_number = f_number.strip()[1:] #would remove anything before the number
    #f_number = f_number.strip()[1:].zfill(2) #to make numbers from single digits to 01, 02 ..can do this with zfill
    print('{}-{}-{}{}'.format(f_number, f_course, f_title, f_ext))

    # You have the power to reformat in any way you see fit
    print('{}-{}{}'.format(f_number, f_title.strip(), f_ext.strip()))

    new_name = '{}-{}{}'.format(f_number, f_title, f_ext)

    os.rename(f, new_name)'''


