# s2 = {'aa','bb',1,2,3,4,5,6,7,8}
# s2.add(1222)
# print(s2)

# p = ['aa', 'bb', 'cc', 'dd']
# s = ['aa', 'bbbb', 'cccc', 'dd']
# r1 = set(p)
# r2 = set(s)

# all element except the duplicate
# print(r1.union(r2))
# print(r1|r2)

# the element which two party have
# print(r1.intersection(r2))
# print(r1&r2)

# the difference from left side
# print(r1.difference(r2))
# print(r1-r2)
# print(r2.difference(r1))
# print(r2-r1)

# (total element - same element they have)
# print(r1.symmetric_difference(r2))
# print(r1 ^ r2)

# r1 have not same element with r2 #return false
# print(r1.isdisjoint(r2))

# r3 is the child of r4, return false
r3={1,2,3}
r4={1,2}
# print(r3.issubset(r4))

# r3 is the parent of r4
print(r3.issuperset(r4))
