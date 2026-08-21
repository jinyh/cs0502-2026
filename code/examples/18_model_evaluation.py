"""L18：用对象重复记录演示随机按行划分的数据泄漏。"""


def accuracy(predictions, labels):
    return sum(prediction == label for prediction, label in zip(predictions, labels)) / len(labels)


def main():
    subjects = list(range(20))
    labels = {subject: subject % 2 for subject in subjects}

    # 错误评价：每个对象一条记录用于训练，另一条记录用于测试。
    memorized_subject_labels = labels.copy()
    leaked_predictions = [memorized_subject_labels[subject] for subject in subjects]
    leaked_truth = [labels[subject] for subject in subjects]

    # 更接近部署：测试对象从未在训练出现，只能使用训练集多数类基线。
    train_subjects = subjects[:10]
    test_subjects = subjects[10:]
    majority_label = max((0, 1), key=lambda label: sum(labels[subject] == label for subject in train_subjects))
    group_predictions = [majority_label for _ in test_subjects]
    group_truth = [labels[subject] for subject in test_subjects]

    print("同一对象跨集合的表面准确率:", f"{accuracy(leaked_predictions, leaked_truth):.0%}")
    print("按对象隔离后的基线准确率:", f"{accuracy(group_predictions, group_truth):.0%}")
    print("第一种结果只证明能记住对象，不能证明能泛化到新对象。")


if __name__ == "__main__":
    main()
