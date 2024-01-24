s = "string"
print(s)
for x in s:
    print(x)
print("s" in s)
if "s" in s:
    print("Ye")
print("k" not in s)
if("k" not in s):
    print("Absofreakinlutely")
print(s[2:5])
print(s[2:])
print(s[:5])
print(s[-5:-2])


print(s.upper())
print(s.lower())

print(s.strip())

print(s.replace("s", "S"))

print(s.split("r"))

a = "kar"

b = "98k"

print(a+b)


k = 3
l = 10
txt = "i wanna buy {1} for {2} liras"
print(txt.format(k,l))

print("my mother told \"me \" some day i will buy")
print('It\'s aight')
print("Hello\nworld!")
print("Hello\rworld!")
print("Hello\bworld!")
print("Hello\tworld!")
