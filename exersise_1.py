# f=open("./input.txt","w")
# f.write("6,7\n7,8\n2,8\n9,5\n9,6")
def sumOfNumber():
  
  with open("./input.txt","r") as f:
    # print(f.read())

    for line in f:
      numbers=[int(x)
               for x in
               line.split(",")]
      total=sum(numbers)
      return total
      # for n in numbers:
      # # print(n)
    #     sum=n[0]+n[1]
    # return sum
    
print("sum:",sumOfNumber())
# f.close()
# f_out.close()