def apply_all_func(int_list: list[int], *functions):
    results = dict()
    for function in functions:
        results[function.__name__] = function(int_list)
    return results


if __name__ == '__main__':
    assert apply_all_func([6, 20, 15, 9], max, min)
    assert apply_all_func([6, 20, 15, 9], len, sum, sorted)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
