# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
import sys
def remove_adjacent(nums):
 newstr=[]
 for num in nums:
  if len(newstr)==0 or num!=newstr[-1]:
   newstr.append(num)
 print(newstr)
   
 return


 
def main():
 remove_adjacent([1, 2, 2, 3])


if __name__ == '__main__':
 main()
