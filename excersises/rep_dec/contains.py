def contains(origin,search):
    is_contained = False
    for term in origin:
        if term.lower() == search.lower():
            is_contained = True
    return is_contained
cities = ["Stockholm", "New York", "Tokyo", "Berlin"]
print(contains(cities, "Tokyo"))
print(contains(cities, "Madrid"))