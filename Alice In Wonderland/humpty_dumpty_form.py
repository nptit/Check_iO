from math import pi, sqrt, asin, degrees, atanh 

def checkio(height, width):
    height = float(height) 
    width = float(width) 
    my_list = []
    if height == width:
        r = 0.5 * width
        surface_area = 4 * pi * r**2
        surface_area = round(surface_area, 2) 
        my_list.append(surface_area)
    elif height > width:  # If spheroid is prolate
        a = 0.5 * width
        b = 0.5 * height
        e2 = 1 - a**2 / b**2
        e = sqrt(e2) 
        surface_area = 2 * pi * a**2 * (1 + b / (a * e) * asin(e))
        my_list.append(round(surface_area, 2))
    elif height < width:  # If spheroid is oblate
        a = 0.5 * width
        b = 0.5 * height
        e2 = 1 - b**2 / a**2
        e = sqrt(e2) 
        surface_area = 2 * pi * a**2 * (1 + (1 - e2) / e * atanh(e))
        my_list.append(round(surface_area, 2))
    return my_list
