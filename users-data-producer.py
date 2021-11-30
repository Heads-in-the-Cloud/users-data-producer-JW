from faker import Faker
from collections import defaultdict
import random
import requests
import json

def username(fname, lname):
    return fname+"-"+lname+ str(random.randint(1000,9999))

def phoneNum():
    n = '0000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        n = str(random.randint(10**9, 10**10-1))
    return n[:3] + '' + n[3:6] + '' + n[6:]
def userRole():
    userRole = defaultdict(list)
    roleId = random.randint(1,3)
    if(roleId==1):
        userRole["id"].append(roleId)
        userRole["name"].append("Administrator")
    elif(roleId==2):
        userRole["id"].append(roleId)
        userRole["name"].append("Employee")
    elif(roleId==3):
        userRole["id"].append(roleId)
        userRole["name"].append("User")
    return userRole
def dataProducer():
    faker = Faker()
    user = defaultdict(list)

    givenName = faker.first_name()
    familyName = faker.last_name()

    user["given_name"].append(givenName)
    user["family_name"].append(familyName)
    user["username"].append(username(givenName,familyName))
    user["password"].append(faker.password())
    user["email"].append(faker.unique.email())
    user["phone"].append(str(phoneNum()))
    user["userRole"].append(userRole())

    userJSON = json.dumps(user)
    userJSON=userJSON.replace("[", "")
    userJSON=userJSON.replace("]","")
    finalinput = json.loads(userJSON)
    response =requests.post("http://localhost:9002/user/register", json=finalinput)

for x in range(10):
    dataProducer()