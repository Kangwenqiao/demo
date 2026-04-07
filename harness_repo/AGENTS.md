# AGENTS.md

## Mission
优先交付可验证、可维护、符合分层约束的改动，而不是只让当前测试通过。

## Always
1. 修改生产代码前，先阅读与任务相关的规范文件。
2. 完成前必须运行可用测试。
3. 不要把领域规则写进 API 层。
4. 不要只修 visible failure，要补齐 canonical username 的完整规则。
5. 输出最终说明时必须写清：
   - 改了什么
   - 为什么这样改
   - 如何验证

## Routing
- 涉及注册/用户名/校验：先读 `docs/product-specs/new-user-onboarding.md`
- 涉及代码放在哪一层：再读 `ARCHITECTURE.md`
- 涉及验收和完成定义：再读 `QUALITY.md`

## Definition of Done
- visible tests 通过
- 没有把标准化/校验逻辑放进 api 层或 service 层
- 至少新增 3 个 visible tests
- visible tests 总数至少为 5
- 新增测试覆盖：分隔符折叠、保留前缀、canonical duplicate
