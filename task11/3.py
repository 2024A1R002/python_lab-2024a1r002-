#find second largest in list
a = list(map(int, input("Enter your numbers: ").split()))

lar = float('-inf')
sec_lar = float('-inf')

for i in a:
    if i > lar:
        sec_lar = lar
        lar = i
    elif i > sec_lar and i != lar:
        sec_lar = i

print(f"Second Largest number is {sec_lar}")