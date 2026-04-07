# ARCHITECTURE.md

## Layer responsibilities

- `api`: 解析输入、调用 service、格式化输出
- `services`: 编排流程，不承载领域规则，也不决定 canonical username
- `domain`: 用户名 canonicalization 与校验规则
- `repositories`: 数据存取

## Hard rules

- 用户名标准化只能在 domain 层定义
- service 和 api 不允许重复实现用户名规则
- `space` / `hyphen` 到 underscore 的转换只能在 domain 层定义
- 连续分隔符折叠规则只能在 domain 层定义
- 重复用户名判断必须基于 canonical username
- 保留名与保留前缀检查属于领域规则，放在 domain 层
