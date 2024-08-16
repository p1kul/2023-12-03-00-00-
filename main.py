def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        cnt = 0
        for i in range(2,result):
            if result % i == 0:
                cnt+=1
        if cnt >= 1:
            print('Составное')
        else:
            print('Простое')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    res = 0
    for i in args:
        res+=i
    return res

result = sum_three(2, 3, 6)
print(result)
