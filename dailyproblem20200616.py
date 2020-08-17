KAPREKAR_CONSTANT = 6174

def num_kaprekar_iterations(n):

  ite = 0
  answer = n
  print("Starting num: ", n)

  def ascDescNum(x, y):
    tempX = str(x)
  
    while len(tempX) != 4:
      tempX += "0" 
    
    tempValue = sorted(list(tempX), reverse = y)
    tempStr = ""
    
    for each in tempValue:
      tempStr += each
      
    return tempStr
  
  while KAPREKAR_CONSTANT != answer:
    print(int(ascDescNum(answer, True)),"-",int(ascDescNum(answer, False)),end="")
    answer = int(ascDescNum(answer, True)) - int(ascDescNum(answer, False))
    print(" =",answer)
    ite += 1

  return str(ite) + " Iterations until Kaprekars constant from the number " + str(n) + "\n"
  
print(num_kaprekar_iterations(1000))
print(num_kaprekar_iterations(123))
print(num_kaprekar_iterations(9812))
print(num_kaprekar_iterations(6174))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)
