def add_with_transform(left, right, transform_func):
    tmp_val = transform_func(left) + transform_func(right)
    return transform_func(tmp_val)
    # transform_func는 add_plus_1 매개변수로 받아옴
def add_plus_1(number):
    return number + 1

ret_val = add_with_transform(2, 3, add_plus_1)
print(ret_val)
