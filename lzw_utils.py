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

    return result


def decompress(compressed):
    """Decompress a list of output ks to a string."""
    from io import StringIO

    # Build the dictionary.
    dict_size = 128
    dictionary = {i: chr(i) for i in range(dict_size)}

    # use StringIO for speed.
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


if __name__ == '__main__':
    message = '''Nory was a Catholic because her mother was a Catholic, and Norys mother was a Catholic because her father 
    was a Catholic, and her father was a Catholic because his mother was a Catholic, or had been.'''

    print('Length of uncompressed message:', len(message.encode()))
    print('Compressing...')

    compressed_message = compress(message)
    encoded_message = bytes(compressed_message)
    print('Length of encoded compressed message:', len(encoded_message))
    print(f'Compression percentage: {len(encoded_message) * 100 / len(message.encode())}%')

    print(encoded_message)
    # Send through network

    decoded_message = [x for x in encoded_message]
    decompressed_message = decompress(decoded_message)
    print(decompressed_message)
