a = ["NoRa", "IsAbEl", "EiNaR"]
def to_upper(words):
    result = []
    for w in words:
        result.append(w.upper())
    return result
def to_lower(words):
    result = []
    for w in words:
        result.append(w.lower())
    return result
print(a)
print(to_upper(a))
print(to_lower(a))