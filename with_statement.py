


#with statement automatically closes file we dont need to close it.
with open("./reading.txt","r") as f:
  print(f.read());

print(f.closed)   #to check file is closed or not it will print true