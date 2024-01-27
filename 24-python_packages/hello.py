
# Define a variable
var = "returning_var"

# Define a function
def hello() -> str:
    """
    Prints 'Hello, World!'
    """
    return "Hello, World!"

# Define a class
class function_class:
    """
    This is a class
    """
    def __init__(self, name: str) -> None:
        """
        Constructor
        """
        self.name = name

    def __str__(self) -> str:
        """
        String representation
        """
        return "Hello, {}!".format(self.name)

# Call function within module
hello()