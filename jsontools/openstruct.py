
def value_wrap(v):
    if isinstance(v, dict):
        return OpenStruct(v)
    elif isinstance(v, list):
        return map(value_wrap, v)
    else:
        return v


class OpenStruct:
    """
    Borrowing an idea from the Ruby folks, this makes a dictionary allow
    . access rather than [] access.
    """
    def __init__(self, wrap):
        #lazy style, easier to write too
        self.__wrap__ = wrap

    def __getattr__(self, i):
        if i in self.__wrap__:
            return value_wrap(self.__wrap__[i])
        else:
            return None

    def __getitem__(self, i):
        return value_wrap(self.__wrap__[i])

    def __str__(self):
        return self.__wrap__.__str__()

    def __repr__(self):
        return self.__wrap__.__repr__()



