from collections import Counter

phones = ["iphon", "Samsungs", "LG", "Iphone", "Iphone", "LG"]

count = Counter(phones)
print(count["LG"])

text = "Ехал Грека через реку видит Грека в реке рак".lower().replace (" ", "")
count = Counter(text)
print(count)