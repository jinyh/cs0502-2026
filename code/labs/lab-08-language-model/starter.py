def train_bigram(text):
    raise NotImplementedError


def next_probabilities(counts, vocabulary, context, smoothing=1):
    raise NotImplementedError


def generate(counts, vocabulary, start, steps=8):
    raise NotImplementedError
