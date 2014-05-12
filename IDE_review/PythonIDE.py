__author__ = 'Eko Wibowo'


class PythonIDE(object):
    """
    A class to hold Python IDE information
    """
    def __init__(self):
        """
        Initialize an IDE with default data
        """
        self.name = 'Untitled'
        self.publisher = 'Unknown'
        self.stars = 0

    def __repr__(self):
        """
        Return a string representation of this object
        """
        return 'Python IDE named %s, created by %s, with rating at %s stars' % (self.name, self.publisher, self.stars)

    def the_best(self):
        """
        Mark this IDE as the best Python IDE there is!
        """
        self.stars = 5