def column_name(n):
  abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
         'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  lenAbc = len(abc)
  listLen = lenAbc-1
  tempValue = ""
  useableNumber = n-1
  mainValue = useableNumber//listLen
  rest = useableNumber%listLen

  if useableNumber <= listLen:
    return abc[useableNumber]

  elif useableNumber > listLen:
    
    return str(abc[mainValue-1])+str(abc[rest-1])
    

print(column_name(25))
print(column_name(26))
print(column_name(27))
print(column_name(28))
print(column_name(500))
# Z
# AA
# AB


#partly done
#infinite
#-AAA AAAAA AAAAAAA AAAAAAAAAAAAAAA
