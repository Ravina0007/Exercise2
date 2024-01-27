#program that asks the user for three integer numbers and  prints out the sum, product, and average of the numbers.

num1 = int(input("Enter the first integer number: "))
num2 = int(input("Enter the second integer number: "))
num3 = int(input("Enter the third integer number: "))
total_sum = num1 + num2 + num3
product = num1 * num2 * num3
average = total_sum / 3
print("The sum of the numbers is: {}".format(total_sum))
print("The product of the numbers is: {}".format(product))
print("The average of the numbers is: {:.2f}".format(average))