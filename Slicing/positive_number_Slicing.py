       #0123456789
name = "SayedMuba Hash"

print(name[0:7])  #In string indexing, the last number is exclusive. So, the number 7 is exclusive.
print(name[3:6])
print(f"{name[0:10]}: How are you")

print(name[3:])  #from 3 until the end 'h'
print(name[:4])  #from 0 (S) to the 4 (e) - Remember; 4 is exclusive

print(name[10:14])
print(name[10:])

print(name[:6] + name[6:])
print(name[:])  #Both the same