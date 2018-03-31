import random

#quicksort a list of objects based on keys, which can be any of 3 values
# done in O(n) time in one pass, and O(1) additional space complexity
def quicksort(x, pivot_index):
    key1_idx, key2_idx, key3_idx, key4_idx = 0, 0, 0, len(x)
    key1_val, key2_val, key3_val = 'key1', 'key2', 'key3'

    while key3_idx < key4_idx:
        if x[key3_idx]['key'] == key1_val:
            x[key2_idx], x[key3_idx] = x[key3_idx], x[key2_idx]
            x[key1_idx], x[key2_idx] = x[key2_idx], x[key1_idx]
            key1_idx, key2_idx, key3_idx = key1_idx + 1, key2_idx + 1, key3_idx + 1
        elif x[key3_idx]['key'] == key2_val:
            x[key2_idx], x[key3_idx] = x[key3_idx], x[key2_idx]
            key2_idx, key3_idx = key2_idx + 1, key3_idx + 1
        elif x[key3_idx]['key'] == key3_val:
            key3_idx += 1
        else:
            key4_idx -= 1
            x[key3_idx], x[key4_idx] = x[key4_idx], x[key3_idx]

    return x

if __name__ == '__main__':
    keys = ['key1', 'key2', 'key3', 'key4']
    values = [0, 1, 2, 3, 4]

    key_values = [{'key': key, 'value': value} for key in keys for value in values]
    random.shuffle(key_values)
    print(quicksort(key_values, 7))