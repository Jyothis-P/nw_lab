import math
import pickle


def compress(uncompressed):
    """Compress a string to a list of output symbols."""

    # Initializing the dictionary.
    dict_size = 128
    dictionary = {chr(i): i for i in range(dict_size)}

    # Initializing the word and the result array.
    w = ""
    result = []

    # Filling the dictionary.
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])

    for car in dictionary:
        print(car, dictionary[car])
    # print(len(uncompressed), len(result))
    return result


def decompress(compressed):
    """Decompress a list of output ks to a string."""
    from io import StringIO

    # Build the dictionary.
    dict_size = 128
    dictionary = {i: chr(i) for i in range(dict_size)}

    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed_message k: %s' % k)
        result.write(entry)

        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result.getvalue()


# How to use:
# compressed_message = compress('TOBEORNOTTOBEORNOTTOBE')
text = '''Nory was a Catholic because her mother was a Catholic, and Norys mother was a Catholic because her father 
was a Catholic, and her father was a Catholic because his mother was a Catholic, or had been.'''
compressed = compress(text)

print(compressed)
# print(max(compressed))
# no_of_bytes = math.ceil(max(compressed) / 256)
# print(no_of_bytes)
# print(pickle.dumps(compressed))
# print('Compressed Length:', len(pickle.dumps(compressed)))
# print('Compressed Length:', len(bytes(compressed)))
# print([x.to_bytes(no_of_bytes, 'little') for x in compressed])
# decompressed = decompress(compressed)
# print('Uncompressed Length:', len(pickle.dumps(decompressed)))
# print('Uncompressed Length:', len(text.encode()))
# print(decompressed)
