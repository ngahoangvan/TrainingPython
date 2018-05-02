def cum_sum(nums):
    total = 0
    cum_sum = []
    for num in nums:
       total += num
       cum_sum.append(total)
    return cum_sum

t = [1, 2, 3]
print(cum_sum(t))