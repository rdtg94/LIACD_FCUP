def sum_all_odds(a, b):
    sum_odds = 0
    start = min(a, b)
    end = max(a, b)
    for i in range(start, end + 1):
        if i % 2 != 0:
            sum_odds += i
    return sum_odds

# print(sum_all_odds(5, 20))
# print(sum_all_odds(20, 5))
# print(sum_all_odds(20, 21))
# print(sum_all_odds(-40, -70))