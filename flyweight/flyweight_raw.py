# 1st version

class Mesh:
    pass
class Texture:
    pass
class Vector:
    pass
class Color:
    pass

class Tree:
    # should be privat
    mesh_ :Mesh
    bark_: Texture
    leaves_:Texture
    position_:Vector
    height_:float
    thickness_:float
    barkTint_:Color
    leafTint_:Color

# Spliting the object in half. First data
