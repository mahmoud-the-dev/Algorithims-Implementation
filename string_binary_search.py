#load the binary_search function from the previous code
from binary_search import binary_search

#load the names from the file
def load_names(filename):
    names = []
    with open(filename) as f:
        for line in f:
            names.append(line.rstrip())
    return names

#a list to test our search function
names_for_search = ['Maya Ellery','Brad Ellery', 'Jack Rainford', 'Destiny Lloyd', 'George Saunders', 'Cadence Woodley', 'Erica Ingram', 'Ronald Ring','Rachael Porter','Andie Mooney']

# we chose the sorted names file cuz the binary search only works with the sorted items 
sorted_names = load_names("./names/sorted.txt")

#to see if it works
for name in names_for_search:
    index = binary_search(sorted_names,name)
    print("index: ",index)


