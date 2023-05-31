import math

def add(num1,num2):
  if(not math.isnan(num1) and not math.isnan(num2)):
    return num1 + num2
  else: 
    return math.nan
    
def subtract(num1,num2):
  if(not math.isnan(num1) and not math.isnan(num2)):
    if(num2<num1):
      return num1-num2
    else:
      return math.nan
  else:
    return math.nan

def multiply(num1,num2):
  if(not math.isnan(num1) and not math.isnan(num2)):
    return int(num1*num2)
  else:
    return math.nan

def divide(num1,num2):
  if(not math.isnan(num1) and not math.isnan(num2)):
    if(num1%num2 == 0 ):
      return int(num1/num2)
    else:
      return math.nan
  else:
    return math.nan