
# TASK ONE:
# You task is to create a collection for "Formercreep's Permanent employees”.   
Formercreep_Permanent_Employees = [  
    "Ali",  "Asad",  "Farah",
    "Shameer",  "Subhan",  "Salar",  "Hafsa",  "Sana",  "Hoora",
    "Ahad",  "Saif",  "Maryam",  "Irfan",  "Furqan",  "Mehrooz"
    ]
print(Formercreep_Permanent_Employees)


# TASK TWO
# Gluty is a new brand that serves limka all over in Pakistan. They are
# serving various flavor of limka. Every month they introduced a "new"
# flavor.
# These are some of its flavors
# Orange, pineapple, grapes, tutyfruty, pepsi, pakola , reditrish .
# Consider yourself as a product manager of Gluty, your task is to update
# their menu on monthly basis. In which collection you serve Gluty',s
# product.

gluty_menu = [  "Orange",  "Pineapple",  "Grapes",  "Tuty Fruty",  "Pepsi",  "Pakola",  "Reditrish"]
new_flavor = "Lemon Lime"
gluty_menu.append(new_flavor)


# TASK THREE
# HooraPharma is a leading diagnostic medical tools provider company
# that serves as a third party to sell the products of "Seimens".
# Hoorapharma signed an agreement with seimens that they only sell
# their products , they are not allowed to sell other company products.
# Currently these products are in their stock
# Ventilator, CTscan , Defibrillator, ECG machine, Patient monitor,
# Syringes, MRI.
# An employee of "Nihon kohden" came to the manager of Hoorapharma
# and asked him to sell their Patient monitor and Defibrillator.
# What do you think Manager of Hoorapharma will accept his offer??
# Make a collection of their previous stock and Guess what will be the
# reply of Hoorapharma's manager.
# HooraPharma's current stock of products

stock = ['Ventilator', 'CTscan', 'Defibrillator', 'ECG machine', 'Patient monitor', 'Syringes', 'MRI']
# Check if Nihon Kohden's Patient monitor and Defibrillator are already in stock
if 'Patient monitor' in stock and 'Defibrillator' in stock:
    print("Patient monitor and Defibrillator are in stock.")
    print("The manager will not accept the offer to sell Nihon Kohden's products.")
else:
    print("Hoorapharma does not currently have Patient monitor and Defibrillator in stock.")
    print("The manager will likely not accept the offer to sell Nihon Kohden's products as it violates the agreement with Siemens.")
