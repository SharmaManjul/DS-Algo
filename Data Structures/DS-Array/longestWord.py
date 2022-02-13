#Find logest word in string: "I love dog so@#$ much!" , output: "love"

#Using library re to use regex and compiling the word finder and then spliting
#into individual array items. Checking max len of each array element and
#converting to string.

def LongestWord(sen):
  import re
  # code goes here
  pattern = re.compile(r'\W+')
  subSen = pattern.split(sen)
  return(''.join(max(subSen, key=len)))

# keep this function call here
print(LongestWord(input()))
