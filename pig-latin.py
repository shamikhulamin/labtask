list1 = []
list2 = []

length = int(input("how many words mate? : "))

for i in range(length):
    a = input(f"[{i+1}/{length}]enter a word : ")
    list1.append(a)

for j in list1:
    for k in j:
        pass