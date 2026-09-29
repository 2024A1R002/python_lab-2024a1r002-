n = int(input("Enter number of seats: "))

seats = list(map(int, input("Enter seat status: ").split()))

group = int(input("Enter group size: "))

found = False

for i in range(n - group + 1):
    if all(seats[i + j] == 0 for j in range(group)):
        allocated = []

        for j in range(group):
            seats[i + j] = 1
            allocated.append(i + j + 1)

        print("Allocated seats:", tuple(allocated))
        print("Updated seats:", seats)

        found = True
        break

if found == False:
    print("Consecutive seats not available")
    print("Original seats:", seats)