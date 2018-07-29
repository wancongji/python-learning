
def setnameproperty(cls, name):
    cls.NAME = name

def setnameproperty(name):
    def wrapper(cls):
        cls.NAME = name
        return cls
    return wrapper

@xxxx('MY CLASS')
class Myclass:
    pass
