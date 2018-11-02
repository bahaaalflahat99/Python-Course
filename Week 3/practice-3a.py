import requests as re

link = "http://data.fixer.io/api/latest"
par = {'access_key':"687e02ae37299e5a0158c46c8249f2de",}
respons = re.get(link , par).json()
print ("list of avilable currencies " +'\n' , respons ['rates'].keys())
while True:
    try: 
        fr = input(" Choose currency from the above to convert from :")
        eurofr = respons["rates"][fr]
        break
    except: 
        print ("Invaled entery. Try again....")

while True:
    try:  
        to = input('Choose a currency to convert to :')
        euroto = respons["rates"][to]
        break
    except: 
        print ("Invaled entery. Try again....")
while True:
    try:         
        amount = float(input("How many you want to convert: "))
        break
    except: 
        print ("Invaled entery. Try again....")
result = (euroto/eurofr) * amount

print(result)
