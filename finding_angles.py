#Write a python program to enter two angles of a triangle and find the third angle. 
angle1=float(input("Enter first angle: "))
angle2=float(input("Enter second angle: "))
third_angle = 180-(angle1+angle2)
print("Third angle of the triangle is : ",third_angle)
