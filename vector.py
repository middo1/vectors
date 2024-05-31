import math


class Vector:

    def __init__(self, magnitude, direction):
        if self.validate_params(magnitude, direction):
            self.magnitude = magnitude
            self.direction = direction
            self.xcomponent = math.cos(self.direction * (2 * math.pi)/360) * self.magnitude
            self.ycomponent = math.sin(self.direction * (2 * math.pi)/360) * self.magnitude

    def validate_params(self, mag, dir):
        if type(mag) not in [int, float]:
            raise TypeError("Magnitude can only be a num or float")
        CONVENTIONAL_DIRECTIONS = {
            "N": 0,
            "W": 270,
            "S": 180,
            "E": 90,
            "NE": 45,
            "NW": 315,
            "SE": 135,
            "SW": 225,
        }
        if type(dir) == str and dir not in CONVENTIONAL_DIRECTIONS:
            raise TypeError("Invalid direction")
        if dir in CONVENTIONAL_DIRECTIONS:
            dir = CONVENTIONAL_DIRECTIONS[dir]
        if type(dir) in [int, float] and (dir < 0 or dir > 360):
            raise TypeError(
                "Invalid Direction: direction cannot be less than 0 or greater than 360"
            )
        return True

    def components(self):
        return (self.xcomponent, self.ycomponent)

    def __str__(self) -> str:
        return f"""magnitude: {self.magnitude}
                   direction: {self.direction}
                   x-component: {self.xcomponent}
                   y-component: {self.ycomponent}

        """

    # def __add__(self, other_vector):
