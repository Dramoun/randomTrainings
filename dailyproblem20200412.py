class Solution:

  def sortColors(self, nums):

    tempList = list()
    stopNum = 0
    
    while stopNum !=3:
      
      for color in nums:

        if color == stopNum:
          tempList.append(stopNum)

      stopNum += 1
      
    print(tempList)
    
x = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

print("Before Sort: ")
print(x)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

print("After Sort: ")
Solution().sortColors(x)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
