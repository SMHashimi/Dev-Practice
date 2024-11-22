from PIL.ImImagePlugin import number  #0123456789
name = "SayedMuba Hash"

print(name[0:6:2])
print(name[0:6:3])

a_million_dollars = "1,000,000"
print(a_million_dollars[1::4])

print(name[3::4]) #It starts indexing from 3, skipping 3 characters and prints the subsequent one.
                  #Again, 4 is exclusive


