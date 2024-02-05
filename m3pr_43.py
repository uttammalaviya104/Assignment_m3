#WAP to read a random line from a file.

import random
file = open("Random_line.txt","w")
file.write("my name is Uttam malaviya\ni am a student\ni am from junagadh.")
file.close()
file = open("Random_line.txt","r")
lines = file.readlines()
print("Random line: ",random.choice(lines))
file.close()
