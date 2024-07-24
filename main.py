#sizin olduğunuz fotografın arka planını silip sadece sizin kalmanızı sağlar
#first paste your .jpg in backgroundremover file
from rembg import remove

your_file=input("enter your .jpg file to remove back ground: ")

input_path = your_file

output_path = "output.png"

with open(input_path,"rb") as i:
    with open (output_path,"wb") as o:
        input_file=i.read()
        output_file = remove(input_file)
        o.write(output_file)