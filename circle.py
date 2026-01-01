import math

def circle_properties(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area, circumference


# Example usage
r = 5
area, circumference = circle_properties(r)

print("Radius:", r)
print("Area:", round(area, 2))
print("Circumference:", round(circumference, 2))
