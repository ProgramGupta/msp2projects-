x = int(input(f'What number is x equal to? (x should be the greater number) - '))
y = int(input(f'What number is y equal to? - '))


def multiply(x,y):
  d = x*y
  return d
def add(x,y): 
  d = x+y
  return d
def subtract(x,y): 
  d = x-y
  return d
def divide(x,y):
  d = x/y
  return d

c = input(f'What operation should we use - Options: multiply, add, subtract, divide - ')
if c == 'multiply':
  k = multiply(x,y)
elif c == 'add':
  k = add(x,y)
elif c == 'subtract':
  k = subtract(x,y)
elif c == 'divide':
  if y == 0:
    k = f"undefined (divide by 0)"
  else:
    k = divide(x,y)

print (k)