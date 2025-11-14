def rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

l = float(input("Enter length: "))
w = float(input("Enter width: "))
a, p = rectangle_area_perimeter(l, w)
print(f'Perimeter = {p}, Area = {a} ')
