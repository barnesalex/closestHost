import re

file_to_check = "hitlist.txt"
counter = 0
regex = "()([a-z0-9\-]+\.[a-z0-9\-]+\.?[a-z0-9\-]+\.[a-z]{2,})"
output_file = open("foundAddresses.txt","w")
file = open(file_to_check, "r")
print "Checking for addresses in " + file_to_check 
for line in file:
  matches = re.match(regex,line)  
  #print matches.group(2)
  counter += 1
  output_file.write(matches.group(2) + "\n")
output_file.close()
print "Printing found addresses to " + repr(output_file)
print "Found " + repr(counter) + " addresses!"
