#The program then prints out the perimeter and area of the rectangle.

#Method 1

#l = float(input("Enter the Length of the Rectangle : "))
#b = float(input("Enter the Breadth of the Rectangle : "))
#area = l * b
#print(f"Area of Rectangle : {area}sq.units")

#Method 2

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)