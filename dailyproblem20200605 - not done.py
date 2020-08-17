def ip_addresses(s, ip_parts=[]):

  if 4 < len(s) < 12:

    tempInt = ""
    tempStr = ""
  
    for each in s:
      
      if int(tempInt + each) < 256:
        tempInt += each

        if each == s[len(s)-1]:
          tempStr += str(each)

      else:

        tempStr += str(tempInt) + "."
        tempInt = each
        
        if each == s[len(s)-1]:
          tempStr += str(each)
          
      print(tempInt)
    ip_parts.append(tempStr)
      
    return ip_parts
  
  else:
    
    return "Not a valid num"
  
print(ip_addresses('15925510103'))
# ['159.255.101.3', '159.255.10.13']


#not done
