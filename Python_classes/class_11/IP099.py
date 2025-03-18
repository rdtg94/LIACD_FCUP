# def future_exceptions(f, a, b):
#     exception_count = 0
#     for x in range(a, b + 1):
#         try:
#             f(x)
#         except Exception:
#             exception_count += 1
#     return exception_count


# print(future_exceptions(lambda x: 1/x, -5, 5))
# print(future_exceptions(lambda x: 1/(abs(x)-2), -5, 5))


def future_exceptions(f, a, b):
    exception_count = 0
    for x in range(a, b + 1):
        try:
            f(x)
        
        except Exception:
            exception_count += 1
    return exception_count

print(future_exceptions(lambda x: 1/x, -5, 5))
print(future_exceptions(lambda x: 1/(abs(x)-2), -5, 5))
