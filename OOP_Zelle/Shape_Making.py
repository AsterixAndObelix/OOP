# Program implementing cube and sphere objects
from Sphere_and_Cube import Sphere, Cube

def main():
    r_input = int(input("Radius of the sphere: \n"))
    s = Sphere(r_input)
    s.surface_area()
    s.volume()

    s_input = int(input("Side length of the cube: \n"))
    c = Cube(s_input)
    c.surface_area()
    c.volume()

main()
