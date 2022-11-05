class JsObject:
    def __init__(self, dictionary : dict) -> None:
        self.__dict__ = dictionary

    def __getitem__(self, value):
        return self.__dict__[value]


my_dict = {'name':'mahdi', 'age':20}

my_dict = JsObject(my_dict)

print(my_dict.age)
print(my_dict['age'])