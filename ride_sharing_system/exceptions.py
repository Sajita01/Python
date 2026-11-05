class InvalidInputError(Exception):
    """Exception raised for invalid input."""
    pass

class NegativeDistanceError(Exception):
    """Exception raised when the distance is negative."""
    pass

class RideHistoryError(Exception):
    """Exception raised when there is an error with the ride history."""
    pass