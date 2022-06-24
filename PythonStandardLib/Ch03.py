import sys
import tempfile
import zipfile

print("Number of arguments: ", len(sys.argv))
print("Arguments: ", sys.argv)

# Remove arguments
sys.argv.remove(sys.argv[0])
print("Arguments: ", sys.argv)

# Sum up the arguments
arguments = sys.argv
summation = 0
for arg in arguments:
    try:
        number = int(arg)
        summation += number
    except Exception:
        print("Bad input")

print("Summation is: ", summation)

# Input
color = input("What is the best color? ")
print(color)

# Open a file
my_file = open("scores.txt", "w")

# Show the attributes
print("The name is "+my_file.name)
print("Mode "+my_file.mode)

# Write to a file
my_file.write("GBJ : 100\nKHD : 99\nBBB : 89")
my_file.close()

# Temporary file
temp_file = tempfile.TemporaryFile()

temp_file.write(b"Save this special number me: 5678")
temp_file.seek(0)
print(temp_file.read())

temp_file.close()

# Manipulate zip files in python
zip_file = zipfile.ZipFile('Some.zip','r')
print(zip_file.namelist())

# Meta data
for meta in zip_file.infolist():
    print(meta)