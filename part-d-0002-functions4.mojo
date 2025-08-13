def main():

    print(mult(11, 10, 9))

    print(mult(-5, 11, 4, 6))



fn mult(*nums: Int) -> Int:

    var m: Int = 1

    for num in nums:

        m *= num

    return m

#990
#-1320
