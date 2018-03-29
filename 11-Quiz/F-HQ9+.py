inp = input()
if ("H" in inp or "Q" in inp or "9" in inp or "+" in inp) and 1 < len(inp) < 100:
    print("YES")
else:
    print("NO")

x = 5
y = 7
temp = x
x = y
y = temp
