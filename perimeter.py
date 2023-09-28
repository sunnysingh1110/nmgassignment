#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def max_area_right_triangle(perimeter):
    # Calculate a using the critical point equation
    a = (perimeter / 2) - (perimeter / (2 + (2 ** 0.5)))
    
    # Calculate b and c using the perimeter equation and Pythagorean theorem
    b = perimeter - a - ((a ** 2) + (a ** 2)) ** 0.5
    c = ((a ** 2) + (b ** 2)) ** 0.5
    
    # Calculate the area of the right-angled triangle
    area = 0.5 * a * b
    
    return area

# Example usage
perimeter = 10
max_area = max_area_right_triangle(perimeter)
print("Maximum Area of Right-Angled Triangle for Perimeter", perimeter, "is", max_area)

