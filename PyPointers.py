#This is an exercise in understanding how python uses pointers under the hood.
var1 = 5
var2 = 5

def address_of(myVariable):
    return (hex(id(myVariable)))

print(address_of(var1))
print(address_of(var2))
var3 = 10 - var1
print(address_of(var3))
var3 = var3 + 1
print(address_of(var3))
