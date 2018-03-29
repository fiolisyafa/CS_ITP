languages = ["swahili", "english", "japanese", "swedish", "indonesian"]

#accessing elements by index
print(languages[0].title())
print(languages[-1].title())
print('My classes are in ' + languages[1].title())

#changing elements
languages[3] = "spanish"
print(languages)

#adding by append
languages.append("arabic")
print(languages)

#adding by .insert()
languages.insert(2, "korean")
print(languages)

#removing usisng del
del languages[4]
print(languages)

#removing using .pop()
popped_languages = languages.pop()
print(popped_languages)
print(languages)

#removing using .remove()
languages.remove("japanese")
print(languages)

#sorting a list temporarily
print(sorted(languages))
print(languages)

#sorting a list by .sort()
languages.sort()
print(languages)
languages.sort(reverse=True)

#reverse order
languages.reverse()

#finding the length
print(len(languages))
