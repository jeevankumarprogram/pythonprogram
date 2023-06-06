address={"name":"jeevan","phone":123654,"city":"madurai"}
print("my name is",address['name'])
print("my phone no is",address['phone'])

address['age']=22
print(address)

del address["city"]
print(address)

clear("address")
print("address")
