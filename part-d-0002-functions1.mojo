def main():

    print(sum_or_mult(1, -11, 21))

    print(sum_or_mult(2, 22, 10))

    print(sum_or_mult(12, 21, 34))


fn sum_or_mult(selection: UInt8, x: Int32, y: Int32) -> Int32:

    if (selection == 1):

        return x + y

    elif (selection == 2) :

        return x * y
    
    else:
        
        return 0

# 10
# 220
# 0
