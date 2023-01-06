from pygame.math import Vector2


class CircularFustrum:
    def __init__(self, parent=None, r=100):
        self.parent = parent
        self.radius = r

    def inside(self, obj):
        if hasattr(obj, "position"):
            if isinstance(obj.position, Vector2):
                if obj.position.distance_to(self.parent.position) < self.radius:
                    return True
        return False
