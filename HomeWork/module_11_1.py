import inspect


def introspection_info(obj):
    info = {
        'type' : type(obj).__name__,
        'attribute' : [attr for attr in dir(obj)],
        'method' : [method for method in dir(object)],
        'module' : inspect.getmodule(object)
    }
    return info

class Sample:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

sample = Sample(31)
info = introspection_info(sample)
print(info)

number_info = introspection_info(42)
print(number_info)