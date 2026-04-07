# Username Onboarding Demo

This repository is a small starter project for an agent coding exercise.

## Task

See `TASK.md`.

## Run checks

```bash
uv sync
bash scripts/run_visible_checks.sh
```

Instructor-only checks:

```bash
bash scripts/run_hidden_checks.sh
.venv/bin/python scripts/score_submission.py
```

## Experiment Flow

```bash
cd baseline_repo
uv sync
bash scripts/run_visible_checks.sh
```

使用同样的简单提示词修复：

```text
请修复注册流程中的用户名规范化问题，并补上必要测试。完成后确保现有测试通过。
```

修复后再执行：

```bash
bash scripts/run_hidden_checks.sh
.venv/bin/python scripts/score_submission.py
```

## Notes

- The starter implementation is intentionally incomplete.
- Visible tests are intentionally narrower than the full business rules.
