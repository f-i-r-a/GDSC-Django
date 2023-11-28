students={}
def add():
    name=input('name: ')
    age=input('age: ')
    gpa=input('gpa: ')
    students[name]=[age,gpa]
    return students
def lis():
    name=input('enter name u want to see: ')
    n=0
    if name in students:
        print('name: '+name)
        student=list(students[name])
        print('age: '+student[0])
        print('gpa: '+student[1])
    else:
        print('student name not found')
def view():
    if students:
        n=0
        for i in students:
            desc=list(students.values())
            print(i)
            print('age: '+desc[n][0])
            print('gpa: '+desc[n][1])
            n+=1
    else:
        print('NO students found')
def update():
    name=input('enter name to edit: ')
    if name in students:
        print('name: '+name)
        desc=students[name]
        print('age: '+desc[0])
        print('gpa: '+desc[1])
        age=input('enter new age: ')
        gpa=input('and now gpa: ')
        students[name]=[age,gpa]
    else:
        print('name not found')
def delete():
    name=input('enter name you want to delete: ')
    if name in students:
        students.pop(name)
        print('succefully deleted ',name)
    else:
       print('name not found')
while 1:
    command=input('1. add\n2. list\n3. view \n4. update \n5. delete\n6. quit \n')
    if command=='1':
        add()
    elif command=='2':
        lis()
    elif command=='3':
        view()
    elif command=='4':
        update()
    elif command=='5':
        delete()
    elif command=='6':
        break
    else:
        print('wrong input') 
