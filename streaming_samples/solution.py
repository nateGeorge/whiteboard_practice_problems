import random

def get_samp(stream, size):
    i = 0
    samp = []
    while i < size:
        samp.append(next(stream))
        i += 1
    for i, el in enumerate(stream):
        if random.random() < 1/float(i + size):
            ix = random.choice(range(size))
            samp[ix] = el

    return samp

if __name__ == "__main__":
    stream = iter(range(200))
    samp1 = get_samp(stream, 1)
    stream = iter(range(200))
    samp5 = get_samp(stream, 5)

    samps = []
    for i in range(100000):
        stream = iter(range(5))
        samps.append(get_samp(stream, 1))

    # check to make sure probability is uniform over values
    import pandas as pd
    sdf = pd.DataFrame(samps)
    print sdf[0].value_counts().sort_index()
