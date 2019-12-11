import base64
value = "VWtkc2EwbEliSFprVTBJeFl6SlZaMWxUUW5OaU1qbDNVSGM5UFE9PQ=="
if len(value) % 4:
# not a multiple of 4, add padding:
    value += '=' * (4 - len(value) % 4)
#count = 0
decodethis = base64.b64decode(value)
print(decodethis)
try2 = base64.b64decode(decodethis)
print(try2)
try3 = base64.b64decode(try2)
print(try3)






#while count > 4:
    #value = "VWtkc2EwbEliSFprVTBJeFl6SlZaMWxUUW5OaU1qbDNVSGM5UFE9PQ=="
 #   newvalue = base64.b64decode(value)
  #  value = newvalue
   # print(value)
    #count += 1
#print(value)