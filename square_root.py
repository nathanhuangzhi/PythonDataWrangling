input_number = 99999

i = 0
while 10**i < input_number:
    i += 2

lower_bound = int(10**(i/2-1))
upper_bound = int(10**(i/2))

for j in range(lower_bound,upper_bound):
    if (j)**2>= input_number:
        break

print(j-1)
print(316**2)

print(317**2)



