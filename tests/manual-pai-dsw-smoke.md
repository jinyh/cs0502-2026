# PAI-DSW 学生运行链路烟雾测试

> 在课程发布前使用教师测试账号执行。不要上传真实学生数据、考题或模型凭据。

## GitHub 可访问路径

1. 新建支持 `/mnt/workspace` 持久化的 Python 3.11+ CPU Notebook。
2. 上传并从头运行 `notebooks/modelscope/CS0502-quickstart.ipynb`。
3. 确认仓库可克隆或快进更新，环境安装完成，首次环境验证全部通过。
4. 分别运行一个 example、初始化并测试一个 Lab、打开一个 HTML 可视化。
5. 确认每次代码运行都生成可复制的 `[CS0502_RESULT]` 摘要。

## ZIP 离线路径

1. 清理教师测试账号中的 `/mnt/workspace/CS0502`，将课程组发布 ZIP 直接解压到该路径。
2. 临时关闭 Notebook 的 GitHub 网络访问，或使用没有 Git 的测试镜像。
3. 从头运行 Quickstart，确认它显示“检测到课程组 ZIP 解压目录”且不尝试执行 Git 命令。
4. 确认依赖安装、完整 smoke tests、example、Lab、HTML 可视化和 `export_student_work()` 均可使用。
5. 确认导出的 ZIP 只包含 `student-work/`，课程包中不含 `LectureNotes/*.pdf` 或 `reference/`。

## 失败提示

1. 用空的 `/mnt/workspace/CS0502` 在无 Git 环境运行，确认提示上传课程组 ZIP。
2. 只放入 `README.md` 后重试，确认提示课程包不完整，并且不会覆盖现有目录。
