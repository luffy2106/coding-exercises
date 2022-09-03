


def name_sex(people):
    return ["Mr. " + person for person in people]


people = ["Huy", "Kien"]

# to understand the meaning of * while calling a function in print, check the 2 following commands :

print(*name_sex(people), sep='\n')
print(name_sex(people), sep='\n')