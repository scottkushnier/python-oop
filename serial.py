"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    Structure:  start (base number to start generating from)
                next  (next number coming up to be generated)

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=1):
        """ Initialize a generator object, optional start value (defaults to 1)"""
        self.start = start
        self.next = start
    
    def generate(self):
        """ Use SerialGenerator object to spit out a new number"""
        ret = self.next
        self.next += 1
        return ret
    
    def reset(self):
        """ Reset the generator object back to the base value, (next generated with be original start value)"""
        self.next = self.start
