class OpenStruct:
    """
    Borrowing an idea from the Ruby folks, this makes a dictionary allow
    . access rather than [] access.
    """
    def __init__(self, dic):
        self.__dict__.update(dic)
        #recurse
        for k, v in dic.iteritems():
            if isinstance(v, dict):
                self.__dict__[k] = OpenStruct(v)

    def __getattr__(self, i):
        if i in self.__dict__:
            return self.__dict__[i]
        else:
            return OpenStruct({})

    def __setattr__(self, i, v):
        if i in self.__dict__:
            self.__dict__[i] = v
        else:
            self.__dict__.update({i: v})
        return v
