from .geometry import Rectangle


class PackingAlgorithm(object):
    """PackingAlgorithm base class"""

    def __init__(self, width, height, weight, rot=True, bid=None, *args, **kwargs):
        """
        Initialize packing algorithm

        Arguments:
            width (int, float): Packing surface width
            height (int, float): Packing surface height
            weight (int, float): Packing surface weight
            rot (bool): Rectangle rotation enabled or disabled
            bid (string|int|...): Packing surface identification
        """
        self.width = width
        self.height = height
        self.weight = weight
        self.rot = rot
        self.rectangles = []
        self.bid = bid
        self._surface = Rectangle(0, 0, width, height, weight)
        self.reset()

    def __len__(self):
        return len(self.rectangles)

    def __iter__(self):
        return iter(self.rectangles)

    def _fits_surface(self, width, height, weight):
        """
        Test surface is big enough to place a rectangle

        Arguments:
            width (int, float): Rectangle width
            height (int, float): Rectangle height
            weight (int, float): Rectangle weight

        Returns:
            boolean: True if it could be placed, False otherwise
        """
        assert(width > 0 and height > 0 and weight > 0)
        if self.rot and (width > self.width or height > self.height):
            width, height = height, width

        if width > self.width or height > self.height or weight > self.weight:
            return False
        else:
            return True
    
    def __getitem__(self, key):
        """
        Return rectangle in selected position.
        """
        return self.rectangles[key]

    def used_area(self):
        """
        Total area of rectangles placed

        Returns:
            int, float: Area
        """
        return sum(r.area() for r in self)

    def used_weight(self):
        """
        Total weight of rectangles placed

        Returns:
            int, float: Weight
        """
        return sum(r.weight for r in self)

    def fitness(self, width, height, weight, rot = False):
        """
        Metric used to rate how much space is wasted if a rectangle is placed.
        Returns a value greater or equal to zero, the smaller the value the more 
        'fit' is the rectangle. If the rectangle can't be placed, returns None.

        Arguments:
            width (int, float): Rectangle width
            height (int, float): Rectangle height
            weight (int, float): Rectangle weight
            rot (bool): Enable rectangle rotation

        Returns:
            int, float: Rectangle fitness 
            None: Rectangle can't be placed
        """
        raise NotImplementedError
        
    def add_rect(self, width, height, weight, rid=None):
        """
        Add rectangle of widthxheight dimensions with weight factor.

        Arguments:
            width (int, float): Rectangle width
            height (int, float): Rectangle height
            weight (int, float): Rectangle weight
            rid: Optional rectangle user id

        Returns:
            Rectangle: Rectangle with placemente coordinates
            None: If the rectangle couldn be placed.
        """
        raise NotImplementedError

    def rect_list(self):
        """
        Returns a list with all rectangles placed into the surface.
        
        Returns:
            List: Format [(x, y, width, height, weight, rid), ...]
        """
        rectangle_list = []
        for r in self:
            rectangle_list.append((r.x, r.y, r.width, r.height, r.weight, r.rid))

        return rectangle_list

    def validate_packing(self):
        """
        Check for collisions between rectangles, also check all are placed
        inside surface.
        """
        surface = Rectangle(0, 0, self.width, self.height, self.weight)

        for r in self:
            if not surface.contains(r):
                raise Exception("Rectangle placed outside surface")

        
        rectangles = [r for r in self]
        if len(rectangles) <= 1:
            return

        if self.used_weight() > self.weight:
            raise Exception("Rectangle weight excess detected")

        for r1 in range(0, len(rectangles)-2):
            for r2 in range(r1+1, len(rectangles)-1):
                if rectangles[r1].intersects(rectangles[r2]):
                    raise Exception("Rectangle collision detected")

    def is_empty(self):
        # Returns true if there is no rectangles placed.
        return not bool(len(self))

    def reset(self):
        self.rectangles = []    # List of placed Rectangles.



