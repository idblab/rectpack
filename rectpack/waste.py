from .guillotine import GuillotineBafMinas
from .geometry import Rectangle



class WasteManager(GuillotineBafMinas):

    def __init__(self, weight, rot=True, merge=True, *args, **kwargs):
        super(WasteManager, self).__init__(1, 1, weight, rot=rot, merge=merge, *args, **kwargs)
   
    def add_waste(self, x, y, width, height):
        """Add new waste section"""
        self._add_section(Rectangle(x, y, width, height, 0))

    def _fits_surface(self, width, height):
        raise NotImplementedError

    def validate_packing(self):
        raise NotImplementedError

    def reset(self):
        super(WasteManager, self).reset()
        self._sections = []
