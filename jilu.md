kangwenqiao@kangwenqiaodeMacBook-Pro baseline_repo % bash scripts/run_visible_checks.sh
.F                                                                                                              [100%]
====================================================== FAILURES =======================================================
_______________________________________ test_normalizes_username_before_storing _______________________________________

    def test_normalizes_username_before_storing() -> None:
        api, repo = build_api()

>       response = api.register({"username": " Alice "})
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_onboarding_visible.py:24:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
src/api/onboarding_api.py:10: in register
    created_username = self.service.register(username)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/services/onboarding_service.py:17: in register
    validated_username = validate_username(candidate)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

username = ' Alice '

    def validate_username(username: str) -> str:
        if len(username) < 3 or len(username) > 20:
            raise ValueError("username must be between 3 and 20 characters")
        if not USERNAME_PATTERN.fullmatch(username):
>           raise ValueError("username may only contain lowercase letters, numbers, and underscores")
E           ValueError: username may only contain lowercase letters, numbers, and underscores

src/domain/user_rules.py:11: ValueError
=============================================== short test summary info ===============================================
FAILED tests/test_onboarding_visible.py::test_normalizes_username_before_storing - ValueError: username may only contain lowercase letters, numbers, and underscores
1 failed, 1 passed in 0.02s
kangwenqiao@kangwenqiaodeMacBook-Pro harness_repo % bash scripts/run_visible_checks.sh
.F                                                                                                              [100%]
====================================================== FAILURES =======================================================
_______________________________________ test_normalizes_username_before_storing _______________________________________

    def test_normalizes_username_before_storing() -> None:
        api, repo = build_api()

>       response = api.register({"username": " Alice "})
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_onboarding_visible.py:24:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
src/api/onboarding_api.py:10: in register
    created_username = self.service.register(username)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/services/onboarding_service.py:17: in register
    validated_username = validate_username(candidate)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

username = ' Alice '

    def validate_username(username: str) -> str:
        if len(username) < 3 or len(username) > 20:
            raise ValueError("username must be between 3 and 20 characters")
        if not USERNAME_PATTERN.fullmatch(username):
>           raise ValueError("username may only contain lowercase letters, numbers, and underscores")
E           ValueError: username may only contain lowercase letters, numbers, and underscores

src/domain/user_rules.py:11: ValueError
=============================================== short test summary info ===============================================
FAILED tests/test_onboarding_visible.py::test_normalizes_username_before_storing - ValueError: username may only contain lowercase letters, numbers, and underscores
1 failed, 1 passed in 0.02s

kangwenqiao@kangwenqiaodeMacBook-Pro harness_repo % bash scripts/run_hidden_checks.sh
.....                                                                                                           [100%]
5 passed in 0.00s
Layer rule check passed.
kangwenqiao@kangwenqiaodeMacBook-Pro harness_repo % .venv/bin/python scripts/score_submission.py
Automated scoring
=================
PASS | Visible tests | 4/4
.....                                                                    [100%]
5 passed in 0.00s

PASS | Hidden tests | 6/6
.....                                                                    [100%]
5 passed in 0.00s

PASS | Architecture check | 4/4
Layer rule check passed.

Automated subtotal: 14/14
Manual review remaining: 6/20
- Change quality: 3 points
- Delivery explanation: 3 points
kangwenqiao@kangwenqiaodeMacBook-Pro harness_repo %

kangwenqiao@kangwenqiaodeMacBook-Pro baseline_repo % .venv/bin/python scripts/score_submission.py
Automated scoring
=================
PASS | Visible tests | 4/4
.....                                                                    [100%]
5 passed in 0.00s

PASS | Hidden tests | 6/6
.....                                                                    [100%]
5 passed in 0.00s

PASS | Architecture check | 4/4
Layer rule check passed.

Automated subtotal: 14/14
Manual review remaining: 6/20
- Change quality: 3 points
- Delivery explanation: 3 points
kangwenqiao@kangwenqiaodeMacBook-Pro baseline_repo %

## 结论

这次记录不能直接说明 harness 相比 baseline 明显更优，主要不是模型没用，而是实验设计和记录口径没有锁住。

当前 `jilu.md` 混入了两种不同阶段的数据：

1. 前半段是修复前结果：两个仓库的 `bash scripts/run_visible_checks.sh` 都失败，且失败栈完全一致。
2. 后半段是修复后结果：`bash scripts/run_hidden_checks.sh` 和 `.venv/bin/python scripts/score_submission.py` 都已经通过。

这意味着当前记录不能拿来比较“同样提示词下 baseline 修得如何、harness 修得如何”，因为它没有把两边各自修复后的结果成对记录下来。

## 为什么这个实验观感不好

1. 起点没有和终点分开记录。
修复前的 visible 失败，与修复后的 hidden/score 通过，被写进了同一段流程里，读起来像是同一次连续结果，但实际上不是同一个阶段。

2. 没有把 baseline 与 harness 的最终 patch 质量并排比较。
如果只看“最后都 14/14”，那实验自然看不出 harness 的优势。

3. visible tests 太弱。
公开测试只暴露一个明显 bug，模型即使没有充分利用 harness 文档，也很可能一次性修好，导致两组结果收敛。

4. 评分项主要是可执行检查，不足以放大 harness 的优势。
如果 hidden tests 和架构检查都能被一个短提示词直接覆盖，`AGENTS.md`、`ARCHITECTURE.md`、`QUALITY.md` 的价值就不容易在分数上体现出来。

5. 当前仓库状态可能已经被多轮修改污染。
从工作区状态看，两个 repo 的源码和 visible tests 都被改过。如果不是每轮都从同一个干净快照开始，结果就不稳定。

## 更合理的实验记录方式

每次实验至少固定记录 4 组结果，并且 baseline / harness 分开写：

1. 修复前 `bash scripts/run_visible_checks.sh`
2. 修复后 `bash scripts/run_visible_checks.sh`
3. 修复后 `bash scripts/run_hidden_checks.sh`
4. 修复后 `.venv/bin/python scripts/score_submission.py`

除此之外，还要额外保存：

1. 模型最终修改了哪些文件
2. baseline 最终 patch
3. harness 最终 patch
4. 最终说明文本

这样才能比较：

1. harness 是否更容易把规则放进正确分层
2. harness 是否更容易补到保留名、标准化后重复名等隐藏规则
3. harness 是否更少改错文件、少走弯路

## 如果要让 harness 优势更明显

1. 不要让 visible tests 直接暴露完整修法。
visible 只提示“标准化有问题”是对的，但 hidden 要覆盖保留名、重复名、层级约束。

2. 强化“质量差异”而不是只看 pass/fail。
例如统计：
生产代码改了几个文件、是否新增了不必要逻辑、是否把规则写进 api/service、是否新增了符合要求的测试。

3. 保持两边起跑线一致，但只让 harness 多出规范文件。
不能让 harness 预先多带公开测试或更强的默认脚本检查，否则优势来源会变成“测试更多”，而不是“文档和约束更好”。

4. 每轮实验都从干净快照恢复。
最稳妥的做法是每次复制一份全新 `baseline_repo` / `harness_repo`，避免前一轮 patch 影响下一轮。

## 当前这份记录可得出的保守结论

只能说明：

1. 两个仓库在修复前暴露的是同一个用户名标准化问题。
2. 在某一轮后续修改之后，两个仓库都能通过 hidden checks 和 score submission。

不能说明：

1. harness 一定比 baseline 修得更好
2. harness 在同样提示词下显著提升了最终得分
3. harness 一定改善了第一次修复成功率

## 下次实验建议

建议把目标从“谁最后都能修好”改成“谁更稳定地一次修好，并且改得更符合约束”。  
如果你要复现实验，最好额外记录这三项：

1. 首次提交是否通过 hidden checks
2. 最终修改文件数
3. 是否违反分层约束
