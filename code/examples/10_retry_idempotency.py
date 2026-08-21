"""L10：对比无去重提交与带请求标识的幂等提交。"""


class ExperimentService:
    def __init__(self):
        self.jobs = []
        self.processed_requests = {}

    def submit_without_id(self, payload):
        job_id = len(self.jobs) + 1
        self.jobs.append((job_id, payload))
        return job_id

    def submit_idempotently(self, request_id, payload):
        if request_id in self.processed_requests:
            return self.processed_requests[request_id]
        job_id = len(self.jobs) + 1
        self.jobs.append((job_id, payload))
        self.processed_requests[request_id] = job_id
        return job_id


def main():
    unsafe = ExperimentService()
    print("无请求 id 的两次返回:", unsafe.submit_without_id("sample-A"), unsafe.submit_without_id("sample-A"))
    print("实际任务数:", len(unsafe.jobs))

    safe = ExperimentService()
    first = safe.submit_idempotently("request-42", "sample-A")
    retry = safe.submit_idempotently("request-42", "sample-A")
    print("幂等重试的两次返回:", first, retry)
    print("实际任务数:", len(safe.jobs))


if __name__ == "__main__":
    main()
