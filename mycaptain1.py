#to find area of circle
radius=float(input())
area=3.14*(radius*radius)
print(area)


#to ask file name and find extension of it


filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
