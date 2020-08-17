class Solution:
  
  def buddyStrings(self, A, B):

    tempList = []
    coolBool = False
    lastNum = ""
    
    if len(A) == len(B):
      
      for each in range(len(A)):

        if A[each] != B[each] and each == len(B)-2:
          print(each)

          if A[each] == B[each+1] and A[each+1] == B[each-1]:
            coolBool = True

          else:
            coolBool = False

          return coolBool
          
    else:
      return "prd"

print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaacbc', 'aaaaaaacb'))
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaac'))
# False


#nefunguje
