def main():

    print(mult(11.87, 10, 9))

    print(mult(-5, 11.5, 4, 6))



fn mult(*nums: Float32) -> Float32:

    var m: Float32 = 1.0

    for num in nums:

        m *= num

    return m

# 1068.2999
# -1380.0

