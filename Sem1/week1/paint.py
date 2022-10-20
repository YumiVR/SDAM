import math

#Defining Variables of PaintCan 
diameter_paint = 15 #cm
hight_paint = 30 #cm
paintcan_coverage = 5.1 #cm^2

#Defining Walls
longwall_length = 40 #m
longwall_height = 3.4 #m
shortwall_length = 30 #m
shortwall_height = 3.4 #m 

#Defining Boxes
length_of_box = 60 #cm
height_of_box = 35 #cm
width_of_box = 30 #cm

#Calculating the Volume
radius_paint = diameter_paint / 2
can_volume =  (math.pi) * radius_paint ** 2 * hight_paint

#Calculating Surface Area of Walls
longwall_area = (longwall_length) * (longwall_height) 
shortwall_area = (shortwall_length) * (shortwall_height)

#Calculating how many cans of paint are needed
total_area = ((longwall_area) * 2)  + ((shortwall_area) * 2)
numofcans = math.ceil((total_area) / (paintcan_coverage))
print ("Number of cans required:", numofcans)

#Calculate Cans in box
length_cans = length_of_box / diameter_paint
width_cans = width_of_box / diameter_paint

cans_in_box = width_cans * length_cans
print ("Number of cans in box:", cans_in_box)

#Calculating How Many boxes needed
boxes_needed = math.floor(numofcans / cans_in_box)
print ("Number of full Boxes:", boxes_needed)

#Calculating Loose Paint cans
loose_paint_cans = numofcans % cans_in_box
print ("Cans not packed in box:", loose_paint_cans)
