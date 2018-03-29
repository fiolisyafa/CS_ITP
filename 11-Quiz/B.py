inp = input()
vowels = ['o', 'y', 'a', 'i', 'u', 'e']
inp = inp.lower()

out = ""
for i in inp:
    if i not in vowels:
        out += "." + i
print(out)
