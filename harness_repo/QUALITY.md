# QUALITY.md

## Acceptance

- 现有 visible tests 必须通过
- 新增测试要覆盖：
  1. spaces + hyphens 折叠为单个 underscore
  2. 保留名前缀
  3. canonical username 重复
- 不允许为了过测试删除已有测试
- 不允许把规则写死在测试里
- 测试补充应放在 `tests/test_onboarding_visible.py`
- 完成后 `tests/test_onboarding_visible.py` 至少应有 5 个测试

## Preferred change shape

- 生产代码改动不超过 3 个文件
- 尽量复用已有函数
- 不要在多个层重复写 regex 或 `strip`/`lower`/`replace` 逻辑
- visible tests 里至少补 1 个异常路径断言
