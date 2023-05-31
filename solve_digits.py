from itertools import permutations
from itertools import product
import math

def it_list(nums,ops):
  lst = []
  for i in range(len(ops)):
    lst.append(nums[i])
    lst.append(ops[i])
  lst.append(nums[-1])
  return lst
      
def create_it_list(nums,ops):
  perm_num = list(permutations(nums))
  perm_ops = list(product(ops,repeat=(len(nums)-1)))
  lst = []
  for pn in perm_num:
    for po in perm_ops:
      lst.append(it_list(pn,po))
    
  return lst

def parenthesis(lst,target):
  loc = lst[0]
  found = False
  for i in range(1,len(lst)-1,2):
    if (loc == target):
      found = True 
      return found,loc,lst[0:i]
    loc = lst[i](loc,lst[i+1])
  return found,loc,lst


def find_solutions(pos_sol,target):
  found = False
  
  for lst in pos_sol:
    #comment out the lines below when you get parenthesis to work
    loc = lst[0]
    found,loc,lst = parenthesis(lst,target)
    if(found):
      return found,lst
     
  lst = [math.nan]
  return found,lst