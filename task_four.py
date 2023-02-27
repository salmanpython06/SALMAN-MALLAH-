# Task 1
# You are selected as a data scientist in Zebtech , the manager assigned
# you a task to create a program to add first ten customer details. The
# manager asked you to create a table that ask 3 major question.
#  Customer name
#  Customer height
#  Customer contact #.
# These questions are asked by first ten customer. Make sure the height
# should be in decimal and authentication of contact number is
# mandatory, only number is allowed
# code: 
name = []
height = []
contact = []

name.append(input('enter your name: '))
height.append(float(input('enter your height: ')))
contact.append(int(input('enter your contact number: ')))

name.append(input('enter your name: '))
height.append(float(input('enter your height: ')))
contact.append(int(input('enter your contact number: ')))

name.append(input('enter your name: '))
height.append(float(input('enter your height: ')))
contact.append(int(input('enter your contact number: ')))

name.append(input('enter your name: '))
height.append(float(input('enter your height: ')))
contact.append(int(input('enter your contact number: ')))

name.append(input('enter your name: '))
height.append(float(input('enter your height: ')))
contact.append(int(input('enter your contact number: ')))

name.append(input('enter your name: '))
height.append(float(input('enter your height: ')))
contact.append(int(input('enter your contact number: ')))

name.append(input('enter your name: '))
height.append(float(input('enter your height: ')))
contact.append(int(input('enter your contact number: ')))

name.append(input('enter your name: '))
height.append(float(input('enter your height: ')))
contact.append(int(input('enter your contact number: ')))

name.append(input('enter your name: '))
height.append(float(input('enter your height: ')))
contact.append(int(input('enter your contact number: ')))

name.append(input('enter your name: '))
height.append(float(input('enter your height: ')))
contact.append(int(input('enter your contact number: ')))

customer_table = {'customer_name': name, 'customer_height': height,
                   'customer_contact': contact }

print(customer_table['customer_name'])


"""
# Task 2
# Design an online admission for Skillvention. The fields are same as 
# mentioned in the admission form 
"""
# code:
name = input('Enter your name: ')
email = input('Enter your email: ')
address = input('Enter your address: ')
course = input('Enter your course: ')
phone = int(input('Enter your phone: '))

form_dict = {"name": name,
             "email":email,
             'address': address,
             'course': course,
             'phone': phone 
        }
print(form_dict)

"""
# Task 3
# Create a login and registration form for your website "Python Agency
"""
# code: 
# registration form
name = input('enter your name: ')
email = input('enter your email: ')
password = input('enter your password: ')

credentials = {'name': name, 'email': email, 'password': password}

# login form:
print('Login Form......\n')
email = input('Enter you email: ')
password = input('Enter you password')

print(f'Is login  successful {email==credentials["email"] and password==credentials["password"]}')
