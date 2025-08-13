def main():

    print("Area calculation 1: ", calculate_area(11))

    print("Area calculation 1: ", calculate_area(11, 3.14))



# An optional argument is one that includes a default value

def calculate_area(radius: Float32, pi: Float32 = 3.0) -> Float32:

    return pi * radius * radius


# Area calculation 1:  363.0
# Area calculation 1:  379.94
