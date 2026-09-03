#write a python program  to make amount in rupees and claculate how manty 500 and 100 notes are needed
amount = int(input("Enter amount: "))
num_500_notes = amount // 500
remaining_amount = amount % 500
num_100_notes = remaining_amount // 100
print(num_500_notes)
print(num_100_notes)
