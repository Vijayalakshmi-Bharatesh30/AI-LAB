room_a = input("Room A : ").lower()
room_b = input("Room B : ").lower()

print("Vacuum is in Room A")

if room_a == "dirty":
    print("Cleaning Room A")
    room_a = "clean"
else:
    print("Room A is already clean")

print("Moving to Room B")

if room_b == "dirty":
    print("Cleaning Room B")
    room_b = "clean"
else:
    print("Room B is already clean")

print("Room A:", room_a)
print("Room B:", room_b)