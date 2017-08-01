class Employee(object):
    def __init__(self, name):
        self.name = name
    # Getter function
    @property
    def name(self): 
        return self._name
    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string') 
        self._name = value
    # Deleter function (optional)
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute") 
