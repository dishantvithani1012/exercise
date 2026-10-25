'''
Dictionary
---------------------------
    Create Dictionary store 10 different types of detail about you. 
    add dob into it.
    display Dictionary
    remove dob from Dictionary 
    get only keys 
    get only values 
    update age key 
    update city key using update method 
    copy Dictionary into another Dictionary using shallow copy technique
    empty copied Dictionary 
    display empty Dictionary 
'''

Dictionary_values ={
    "Name":"Dishant",
    "Surname":"Vithani",
    "Age":21,
    "Weight":48.5,
    "Gender":"Male",
    "City":"Bhavnagar",
    "Specilization":"AIDS",
    "Pincode":364002,
    "Stream":"MCA",
    "Mo":8141345706
}

print(Dictionary_values)

#add dob into it.
#Dictionary
Dictionary_values["DOB"] ="10/12/2005"
print(Dictionary_values )

#remove dob from Dictionary 

del Dictionary_values["DOB"]
print(Dictionary_values)

#get only keys 

print(Dictionary_values.keys())

#get only values 
print(Dictionary_values.values())

#update age key 

Dictionary_values["Age"]=22
print(Dictionary_values)

#update city key using update method 

Dictionary_values.update({"City":"Ningala"})

print(Dictionary_values)

#copy Dictionary into another Dictionary using shallow copy technique

Dictionary_copy = Dictionary_values.copy()
print(Dictionary_copy)

#empty copied Dictionary 
Dictionary_copy.clear()

#display empty Dictionary 
print(Dictionary_copy)
