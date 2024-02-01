zoznam2 = ["a", "b", "c", "a", "b", "a","b","b"]
def most_frequent(zoznam):
    pocet = 0
    najcastejsie = ""
    for i in zoznam2:
        if zoznam2.count(i) > pocet:
            pocet = zoznam2.count(i)
            najcastejsie = i
    return najcastejsie
print(most_frequent(zoznam2))
