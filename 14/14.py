collatz = {}
longest = 1
longest_cnt = 1

for i in range(1, 1000000):
    cur = i
    current_chain = [cur]
    last_step = -1
    while cur != 1:
        if cur in collatz:
            last_step = collatz[cur]
            break
        if cur % 2 == 0:
            cur = cur // 2
        else:
            cur = 3 * cur + 1
        current_chain.append(cur)
    # Add the elements in the chain to the dict.
    if last_step == -1:
        last_step = 0
    for k in range(len(current_chain)):
        collatz[current_chain[k]] = len(current_chain) - k - 1 + last_step
    if longest_cnt < collatz[i]:
        longest_cnt = collatz[i]
        longest = i
print(longest, longest_cnt)