

'''First lecture from Nazarbayev'''

# We have a vector in 3D, we have its components
# we want to calculate the magnitude

# First ask user for components

x = float(input("Enter x component: "))

y = float(input("Enter y component: "))

z = float(input("Enter z component: "))


print("The x-component you entered is: ", x)
print("The y-component you entered is: ", y)
print("The z-component you entered is: ", z)

# Magnitude

r = (x**2 + y**2 + z**2)**0.5

print("Magnitude of vector is: %8.3f" %r)




