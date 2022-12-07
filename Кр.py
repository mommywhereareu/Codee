from re import sub  

class NameConverter():
    def __init__(self, name, capitalize_first):
        self.name = name
        self.capitalize_first = capitalize_first

    def to_snake_case(self):
        res = [self.name[0].lower()]
        for c in self.name[1:]:
            if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ-'): 
                res.append('_')
                res.append(c.lower())
            else:
                res.append(c)
            if c in ('-'):
                res.remove('-')
        return ''.join(res)

    def to_camel_case(self):
        if capitalize_first == True:
            self.name = sub(r"(_|-)+", " ", self.name).title().replace(" ", "")
            return self.name[0].title() + self.name[1:]
        else:
            self.name = sub(r"(_|-)+", " ", self.name).title().replace(" ", "")  
            return self.name[0].lower() + self.name[1:]


if __name__ == '__main__':
    capitalize_first= True
    name = input()
    reg = NameConverter(name, capitalize_first)
    print(name)
    print(reg.to_snake_case())
    print(reg.to_camel_case())