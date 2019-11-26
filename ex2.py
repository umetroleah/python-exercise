import sys
arguments = sys.argv

def isWhiteLine(line):
  for i in range(len(line)):
    if line[i] !=" " and line[i]!="\t":
      return False
  return True

for str in arguments
  if(!isWhiteLine(str))
    print str
