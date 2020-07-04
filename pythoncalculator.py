# Why do we create a class?
# create a class with keyword class
# naming convention for creating a class is to capitalise the first letter

class Python_Calculator:

    def __init__(self, *nums):  # initialising our class
        self.nums = nums

    def __multiply(self, *nums):
        result = nums[0]
        for num in nums[1:]:
            result *= num
        return print(result)

    def divide(self, *nums):
        result = nums[0]
        for num in nums[1:]:
            result /= num
        return print(result)

    def modulo(self, *nums):
        if len(nums) > 2: # Modulo can only be performed with 2 numbers
            return print("you have chosen too many numbers for this function")
        elif (nums[0] % nums[1] == 0):
            return print(True)
        else:
            return print(False)

    def addition(self, *nums):
        result = 0
        for num in nums:
            result += num
        return print(result)

    def subtraction(self, *nums):
        result = nums[0]
        for num in nums:
            result -= num
        return print(result)

    def area_calculator(self, *nums):
        if len(nums) > 2: # Modulo can only be performed with 2 numbers
            return print("you have chosen too many numbers for this function")
        else:
            print(0.5*nums[0]*nums[1])


    def cm_to_inches(self):
        mode = float(input(
            "Enter 1 for inches to cm: \nEnter 2 for cm to inches: "))  # user input for which conversion they want
        if mode == 1:
            inches = float(input("how many inches? "))
            return print(inches * 2.54)
        elif mode == 2:
            cm = float(input("how many cm? "))
            return print(cm / 2.54)



# testing if it works
# p1 = Python_Calculator()
#
# p1.addition(6, 8, 10)
# p1._Python_Calculator__multiply(6, 9, 10)
# p1.divide(100, 5, 20)
# p1.modulo(100, 50, 50)
# p1.area_calculator(25, 10)
# p1.cm_to_inches()

