nums = [2,2,1]
print(sum(set(nums)) * 2 - sum(nums))
# when we apply set on nums it's remove duplicate number (contains only single value (no duplicates))
# so sum(1+2)*2-sum(2+2+1)

num1 = [4,1,2,1,2]
print(sum(set(num1)) * 2 - sum(num1))

num2 = [1]
print(sum(set(num2)) * 2 - sum(num2))