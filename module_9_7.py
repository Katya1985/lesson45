def is_prime(func):
    def wrapper(*args, **kwargs):
        summ = func(*args, **kwargs)
        is_prime = True
        for i in range(2, summ):
            if summ % i == 0:
                is_prime = False
        if is_prime == True:
            return (f"{summ} Простое")

        else:
            return (f"{summ} Составное")

    return wrapper


@is_prime
def sum_three(*value):
    summ = sum(value)
    return summ


result = sum_three(2, 3, 6)
print(result)
