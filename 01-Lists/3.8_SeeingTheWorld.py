places = ["London", "NYC", "Russia", "Japan", "HongKong"]
print(places)
#temporary alphabetical order
print(sorted(places))
print(places)

#temporary reverse alphabetical order
rev = sorted(places)
rev.reverse()
print(rev)
print(places)

#permanently reversed
places.reverse()
print(places)
#back to original
places.reverse()
print(places)

#permanent alphabetical order
places.sort()
print(places)
#permanent reverse alphabetical order
places.sort(reverse=True)
print(places)
