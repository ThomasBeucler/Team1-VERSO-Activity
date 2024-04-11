a, b = 0, 1
#removed semicolon from line 3
sum_even = 0
# Only sum fibonacci values up to 4,000,000
#changed <= to < 
while b < 4000000:
    #changed / to %
    if b % 2 == 0:
        sum_even += b
    #changed b, b to b, a+b
    a, b = b, a + b

print(sum_even)

# answer should be 4613732
