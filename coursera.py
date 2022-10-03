largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        num == int
    except:
        print('Invalid input')

    if num == "done":
        break

    if largest is None:
        largest = num
    elif num > largest:
        largest = num

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)