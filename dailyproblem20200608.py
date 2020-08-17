def is_palindrome(n):

  strNum = str(n)
  numLen = len(strNum)
  
  if numLen%2 == 1:
    midPoss = int((numLen-1)/2)

    if strNum[:midPoss] == (strNum[midPoss+1:])[::-1]:
      return True

    else:
      return False

  elif numLen%2 == 0:
    midPoss = int(numLen/2)

    if strNum[:midPoss] == (strNum[midPoss:])[::-1]:
      return True

    else:
      return False
    
print(is_palindrome(1234321))
# True
print(is_palindrome(1234322))
# False
print(is_palindrome(123321))
# True
print(is_palindrome(123322))
# False
