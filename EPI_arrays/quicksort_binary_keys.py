import random

#quicksort a list of objects based on keys, which can be any of 3 values
# done in O(n) time in one pass, and O(1) additional space complexity
def quicksort(x, pivot_index):
    false_idx, true_idx = 0, len(x)

    while false_idx < true_idx:
        if not x[false_idx]['key']: # key is False
            false_idx += 1
        else: # key is True
            true_idx -= 1
            x[false_idx], x[true_idx] = x[true_idx], x[false_idx]

    return x

if __name__ == '__main__':
    keys = [True, False]
    values = [0, 1, 2, 3, 4]

    key_values = [{'key': key, 'value': value} for key in keys for value in values]
    random.shuffle(key_values)

    print(quicksort(key_values, 7))