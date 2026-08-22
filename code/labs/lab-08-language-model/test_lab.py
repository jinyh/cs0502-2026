from starter import generate, next_probabilities, train_bigram


def test_smoothed_distribution():
    counts, vocabulary = train_bigram("计算计算验证")
    probabilities = next_probabilities(counts, vocabulary, "计")
    assert abs(sum(probabilities.values()) - 1) < 1e-9
    assert all(value > 0 for value in probabilities.values())
    unseen = next_probabilities(counts, vocabulary, "未")
    assert abs(sum(unseen.values()) - 1) < 1e-9
    assert len(set(round(value, 12) for value in unseen.values())) == 1


def test_deterministic_generation():
    counts, vocabulary = train_bigram("ababac")
    assert generate(counts, vocabulary, "a", steps=3) == generate(counts, vocabulary, "a", steps=3)
