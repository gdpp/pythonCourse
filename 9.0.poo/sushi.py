"""
A module related to the joy of sushi.
No fishy code found here!
"""

def fish():
    """
    Determines if fish is a good meal choice.
    Always returns True, because it always is.
    """

    return True

def Salmon():
    """
    Blueprint for a salmon object
    """
    
    def __init__(self):
        self.tastiness = 10
    
    def bake(self):
        """
        Bake the fish and oven
        """
        
        self.tastiness += 1