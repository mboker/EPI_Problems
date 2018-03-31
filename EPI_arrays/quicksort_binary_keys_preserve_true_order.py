import random


#quicksort a list of objects based on keys, which can be any of 3 values
# done in O(n) time in one pass, and O(1) additional space complexity
def quicksort(x):
    false_idx, array_idx, true_idx = -1, len(x)-1, len(x)-1

    # while false_idx < true_idx:
    #     if x[true_idx]['key']: # key is True
    #         true_idx -= 1
    #     else: # key is False
    #         false_idx += 1
    #         x[false_idx], x[true_idx] = x[true_idx], x[false_idx]
    while array_idx >= 0:
        if x[array_idx]['key']: # key is True
            x[array_idx], x[true_idx] = x[true_idx], x[array_idx]
            array_idx, true_idx = array_idx - 1, true_idx - 1
        else: # key is false
            array_idx -= 1

    return x

if __name__ == '__main__':
    keys = [True, False]
    values = [0, 1, 2, 3, 4]

    key_values = [{'key': key, 'value': value} for key in keys for value in values]
    random.shuffle(key_values)

    print("Original order: ", key_values)
    print("Sorted order: ", quicksort(key_values))