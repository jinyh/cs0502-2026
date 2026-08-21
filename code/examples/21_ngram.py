"""Slide21：字符级二元语言模型与拉普拉斯平滑。不是 BPE。"""

from collections import Counter, defaultdict


def train_bigram(text):
    counts = defaultdict(Counter)
    vocabulary = sorted(set(text))
    for current, following in zip(text, text[1:]):
        counts[current][following] += 1
    return counts, vocabulary


def next_probabilities(counts, vocabulary, context, smoothing=1):
    row = counts[context]
    denominator = sum(row.values()) + smoothing * len(vocabulary)
    return {token: (row[token] + smoothing) / denominator for token in vocabulary}


def generate(counts, vocabulary, start, steps=8):
    result = [start]
    current = start
    for _ in range(steps):
        probabilities = next_probabilities(counts, vocabulary, current)
        current = max(probabilities, key=lambda token: (probabilities[token], token))
        result.append(current)
    return "".join(result)


if __name__ == "__main__":
    model, vocab = train_bigram("计算机科学帮助工程计算计算需要验证")
    distribution = next_probabilities(model, vocab, "计")
    top = sorted(distribution.items(), key=lambda item: (-item[1], item[0]))[:3]
    print("P(next | 计) 前三项:", [(token, round(probability, 3)) for token, probability in top])
    print("确定性生成:", generate(model, vocab, "计"))
