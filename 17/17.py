num_to_str = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",
    100 : "hundred",
    1000 : "onethousand"
}

def num_to_text(n) :
    s = ""
    if n == 0:
        return ""
    elif n <= 20:
        return num_to_str[n]
    elif n < 100:
        s = num_to_str[n // 10 * 10]
        if n % 10 != 0:
            s += num_to_str[n % 10]
    elif n < 1000:
        s = num_to_str[n // 100] + num_to_str[100]
        if n % 100 != 0:
            s += "and" + num_to_text(n % 100)
    elif n == 1000:
        s = num_to_str[1000]
    return s

cnt = 0
for i in range(1, 1001):
    print(num_to_text(i))
    cnt += len(num_to_text(i))
print(cnt)