def train_bigram(text):
    """返回字符二元计数字典和排序后的字符词表；空文本词表为空。"""
    raise NotImplementedError


def next_probabilities(counts, vocabulary, context, smoothing=1):
    """返回给定上下文的平滑下一字符分布；smoothing 必须为正数。"""
    raise NotImplementedError


def generate(counts, vocabulary, start, steps=8):
    """每步选择最高概率字符，同分按字典序；返回含 start 的文本。"""
    raise NotImplementedError
