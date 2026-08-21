"""L20：可检查的本地词项检索、拒答与引用，不调用外部模型。"""


DOCUMENTS = [
    {"id": "card-graph", "text": "BFS 使用 队列 按层 遍历 无权图 最短边数路径"},
    {"id": "card-security", "text": "工具调用 使用 最小权限 参数验证 允许列表 审计日志"},
    {"id": "card-evaluation", "text": "机器学习 测试集 必须 独立 避免 数据泄漏"},
]


def tokenize(text):
    return {token.strip("，。！？:：").lower() for token in text.split() if token.strip()}


def retrieve(query, documents, top_k=2):
    query_tokens = tokenize(query)
    scored = []
    for document in documents:
        overlap = len(query_tokens & tokenize(document["text"]))
        scored.append((overlap, document))
    return [document for score, document in sorted(scored, key=lambda item: item[0], reverse=True)[:top_k] if score > 0]


def answer(query):
    evidence = retrieve(query, DOCUMENTS)
    if not evidence:
        return "本地资料没有足够证据，拒绝作答。", []
    summary = "；".join(document["text"] for document in evidence)
    citations = [document["id"] for document in evidence]
    return f"候选证据摘要：{summary}", citations


def main():
    for query in ("BFS 为什么 使用 队列", "工具调用 如何 限制 权限", "量子纠缠 如何工作"):
        response, citations = answer(query)
        print("查询:", query)
        print(response)
        print("引用:", citations or "无")


if __name__ == "__main__":
    main()
