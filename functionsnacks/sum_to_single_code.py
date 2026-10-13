#     sum = 0
#     counter = 0
#     while number >= 10:
#         digit = number % 10
#         sum += digit
#         number //= 10
#         counter += 1
#     return sum
#
# def sum_digit_to_single_number(digits):
#     sum_1 = 0
#     counter1 = 0
#
#     while digits > 0:
#         digit = digits % 10
#         sum_1 += digit
#         digits = digits // 10
#         counter1 += 1
#     return final_number(sum_1)


# def sum_digit_to_single_number(digits):
#     while digits >= 10:
#         sum_1 = 0
#         while digits > 0:
#             digit = digits % 10
#             sum_1 += digit
#             digits //= 10
#             digits = sum_1
#
#
#     return digits
#

def sum_digit_to_single_number(digits):
    if digits == 0:
        return 0
    return (digits - 1) % 9 + 1


print(sum_digit_to_single_number(9875))
