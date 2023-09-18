import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###
def print_words(wordfile):
 list4=read_file(wordfile)
 dict={}
 dict1={}
 i=1
 for word in list4:
  if word not in dict.values():
   dict[i]=word
   i+=1
 
 for k,word in dict.items():
  j=1
  n=0
  for w in list4:
   if w==dict[k]:
    dict[k]=w
    dict1[k]=j
    j+=1
 for k,word in dict.items(): 
   print(dict[k] + " " + str(dict1[k]))  
    

def print_top(wordfile):
 list4=read_file(wordfile)
 print(list4) 




def read_file(wordfile):
 f = open(wordfile, 'rt', encoding='utf-8')
 list1=[]
 list2=[]
 list3=[]
 for line in f: 
  list1=line.split()
  list2.extend(list1)
 for word in list2:
  list3.append(word.lower())
 list4=sorted(list3)
 f.close()
 return list4
 
 
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
