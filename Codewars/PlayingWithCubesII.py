class Cube(object):
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args
    def __init__(self, _side = 0):
        self._side = _side
    
    def get_side(self):
        """Return the side of the Cube"""
        return abs(self._side)

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self._side = new_side