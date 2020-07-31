#Func to find out the Even Number
# using a list
def is_Even(num_list):
  #define a new local emply lsit to store the even numbers
  new_l =[]
  for nu in num_list:
    if nu % 2 == 0:
       #appending the even nos to new list
      new_l.append(nu)
     else:
      pass
   # Nwo it should return the new updated list created using for loop ouside, so return the list created 
   return new_l
  
new_even = is_Even([2,3,4,5,6,7,8])
#print the new list
print(new_even)

# finding odd/even in range of numbers

def no_even(nmm):
  if nmm % 2 == 0:
    return nmm
  else:
    pass
  
for i in range(2,21):
  print(no_even(i))
    
