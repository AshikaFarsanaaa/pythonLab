from graphics.rectangle import area1 as rect_area, perimeter1 as rect_peri
from graphics.circle import area as circle_area, perimeter as circle_peri
from graphics.threedgraphics.cuboid import surface_area1 as cuboid_area, volume1 as cuboid_vol
from graphics.threedgraphics.sphere import surface_area as sphere_area, volume as sphere_vol

print("Rectangle Area:", rect_area(10, 5))
print("Rectangle Perimeter:", rect_peri(10, 5))

print("Circle Area:", circle_area(7))
print("Circle Perimeter:", circle_peri(7))

print("Cuboid Surface Area:", cuboid_area(2, 3, 4))
print("Cuboid Volume:", cuboid_vol(2, 3, 4))

print("Sphere Surface Area:", sphere_area(3))
print("Sphere Volume:", sphere_vol(3))
