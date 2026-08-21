"""L15：保持检测性能不变，观察基率如何改变阳性预测值。"""


def expected_confusion_matrix(population, prevalence, sensitivity, specificity):
    actual_positive = population * prevalence
    actual_negative = population - actual_positive
    true_positive = actual_positive * sensitivity
    false_negative = actual_positive - true_positive
    true_negative = actual_negative * specificity
    false_positive = actual_negative - true_negative
    return true_positive, false_positive, false_negative, true_negative


def positive_predictive_value(true_positive, false_positive):
    return true_positive / (true_positive + false_positive)


def main():
    population = 10_000
    sensitivity, specificity = 0.90, 0.95
    for prevalence in (0.01, 0.10, 0.50):
        tp, fp, fn, tn = expected_confusion_matrix(population, prevalence, sensitivity, specificity)
        ppv = positive_predictive_value(tp, fp)
        print(
            f"基率 {prevalence:.0%}: TP={tp:.0f}, FP={fp:.0f}, "
            f"FN={fn:.0f}, TN={tn:.0f}, 阳性预测值={ppv:.1%}"
        )


if __name__ == "__main__":
    main()
