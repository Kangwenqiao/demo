# New User Onboarding

## Username policy

注册时用户名会被 canonicalize：

- trim whitespace
- lowercase
- replace one or more spaces / hyphens with a single underscore
- trim leading / trailing underscores after separator normalization

canonical username 必须满足：

- 长度 3-20
- 仅允许 a-z, 0-9, underscore

以下名称保留，不可注册：

- admin
- root
- system

以下前缀同样保留，不可注册：

- admin_
- root_
- system_

重复用户名判断以 canonical username 为准。

例如：

- ` Alice-Smith `
- `alice_smith`
- `ALICE   SMITH`

这三者应视为同一个用户名。

再例如：

- ` Team --- Lead `
- `team_lead`

这两者也应视为同一个用户名。
