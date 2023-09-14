import math
import time

print("Program: XYZ Parsing Program\n\n")
print("Description: This program will scan any text file for x, y, and z coordinate data. Please ensure your data is initially in format x:num y:num z:num (no spaces between colon and number, but spaces between data). This program will parse the entire document for this format and create an output file with just the x, y, and z coordinate data.\n\n")
filePath = input("Please enter location of file:")
outputPath = input("Please enter location of output:")
time.sleep(1);
# opening the text file 
try: 
    file = open(filePath,'r+t')
except IOError:
    print("File could not be opened!")
try: 
    output = open(outputPath + "CorrectedData.txt",'r+t')
except IOError:
    print("File could not be opened!")

time.sleep(1)
print("\nFile opened sucessfully!")
time.sleep(1)
print("\nData Sucessfully Processed and Converted to Radians!")
time.sleep(1)
print("\nOutput Location:" + outputPath + "CorrectedData.txt\n\n")
    
# reading each line     
for line in file: 
    # reading each word         
    for word in line.split(): 
        # displaying the x - axis            
        if "x:" in word:
            j = 0
            wordString = ""
            for j in range(len(word)):
                    
                if j > 1:
                    wordString = wordString + word[j]
                    j += 1
                
            degree = int(float(wordString))
            radians = degree * (3.14159 / 180)
            output.write(str(radians))
            
        # displaying the y - axis            
        if "y:" in word:
            j = 0
            wordString = ""
            for j in range(len(word)):
                if j == 2:
                    output.write(",")
                    
                if j > 1:
                    wordString = wordString + word[j]
                    j += 1
                
            degree = int(float(wordString))
            radians = degree * (3.14159 / 180)
            output.write(str(radians))
                
        # displaying the z - axis            
        if "z:" in word:
            j = 0
            wordString = ""
            for j in range(len(word)):
                if j == 2:
                    output.write(",")
                    
                if j > 1:
                    wordString = wordString + word[j]
                    j += 1
                        
            degree = int(float(wordString))
            radians = degree * (3.14159 / 180)
            output.write(str(radians))                
            output.write("\n")
          
file.close()
output.close()
