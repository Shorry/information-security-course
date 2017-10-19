import math

x = int(input("Input X: "))
n = int(input("Input N: "))

if(x > n * n):
  print("Введенные данные не соответствуют условию X < N * N")
else:
  simple_numbers = []
  simple_numbers.append(2)
  for i in range(3, math.ceil(math.sqrt(x))):
    tmp = True
    for element in simple_numbers:
        if(i % element == 0):
            tmp = False
            break
            
    if(tmp):
        simple_numbers.append(i)
#  print(simple_numbers)
  divtmp = []
  issimple = True
  for element in simple_numbers:
    if(x % element == 0 and x != element):
      issimple = False
      divtmp.append(element)
  if(issimple):
    print(x, " - простое число")
  else:
    print(x, " - не простое число, делители: ", divtmp)