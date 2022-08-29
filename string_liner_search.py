def load_names(filename):
    names = []
    with open(filename) as f:
        for line in f:
            names.append(line.rstrip())
    return names

def index_of_item(collection,target):
    for i in range(0,len(collection)):
        if collection[i] == target:
            return i
    return None


unsorted_names = load_names("./names/unsorted.txt")
names_for_search = ['Maya Ellery','Brad Ellery', 'Jack Rainford', 'Destiny Lloyd', 'George Saunders', 'Cadence Woodley', 'Erica Ingram', 'Ronald Ring','Rachael Porter','Andie Mooney']

for name in names_for_search:
    index = index_of_item(unsorted_names,name)


# print(unsorted_names)