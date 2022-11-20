
user_input = input()

tokens = user_input.split()

nums = []

for pos, token in enumerate(tokens):
    nums.append(int(token))
    max_is = max(nums)

sum = 0

for num in nums:
    sum += num
    
    avg = sum // len(nums)

print(f'{avg} ', end='')

print(max_is)