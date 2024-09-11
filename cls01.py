def closest_to_zero(numbers):
    closest = numbers[0]  

    for num in numbers:
        if abs(num) < abs(closest):  
            closest = num

    return closest

numbers = [-6,4,5,1,3]
closest_number = closest_to_zero(numbers)
print(f"The number closest to zero is: {closest_number}")