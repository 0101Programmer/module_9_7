def is_prime(func):
    def wrapper(*args):
        func_res = func(*args)
        for _ in range(2, func_res):
            if func_res % _ == 0:
                prime_res = f'{func_res} - составное'
            else:
                prime_res = f'{func_res} - простое'
            return prime_res

    return wrapper


@is_prime
def sum_three(one, two, three):
    return one + two + three


s = sum_three(1, 1, 1)
print(s)

s2 = sum_three(2, 2, 2)
print(s2)

s3 = sum_three(1, 5, 2)
print(s3)

s4 = sum_three(1, 5, 5)
print(s4)
