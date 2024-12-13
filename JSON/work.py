book={}

book["Bob"]={
  "name" :"bob",
  "address" : "pink street",
  "phone no" :334354544
}

book["Rob"]={
  "name":"rob",
  "address":"light street",
  "phone no":123342535
}

import json
s=json.dumps(book)            #it will take book as input, dump convert it in string json will convert it in json format
with open("./test.txt","w") as f:
  f.write(s)