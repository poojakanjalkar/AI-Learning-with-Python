def countNum(num):
  count=0
  with open("./input.txt","r") as f:
    for line in f:
      numbers=line.split(",")
      for n in numbers:
        if int(n)==num:
          count+=1
    return count
print("number of occurence",countNum(9))    
