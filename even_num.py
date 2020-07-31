#Func to find out the Even Number
def is_Even(num_list):
  new_l =[]
  for nu in num_list:
    if nu % 2 == 0:
      new_l.append(nu)
     else:
      pass
   return new_l
  
new_even = is_Even([2,3,4,5,6,7,8])
print(new_even)
