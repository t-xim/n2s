a = [1,2,3]
b = a
b.append(4)

# a now == [1,2,3,4]
# To not have this happen assign b as

b = list(a)
