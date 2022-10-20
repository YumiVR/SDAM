print("Surface Area & Volume Calculator")

width = int(input("Input the Width of the Cuboid "))
length = int(input("Input the length of the Cuboid "))
height = int(input("Input the Height of the Cuboid "))

#SA=2lw+2lh+2hw

lw = (length * width) * 2
lh = (length * height) * 2
hw = (height * width) * 2

volume = length * width * height
surfacearea = lw+lh+hw
print ("Surface area =", surfacearea,"CM^2")
print ("Volume =", volume,"CM^3")
