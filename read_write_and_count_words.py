

f=open("./reading.txt","r")
f2=open("./reading_count.txt","w")
for word in f:
  tokens=word.split(" ")
  f2.write("wordcount: "+str(len(tokens))+" "+word)
  
  
f.close()
f2.close()