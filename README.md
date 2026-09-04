# AI 项目仓库模板

本模板为 AI 开发项目提供最小化的 GitHub 治理基础。

## 文件说明

- `.git-management.json`：仓库治理策略，定义分支格式、必需检查、可选 Review 和合并方式。
- `.github/workflows/ci.yml`：通用项目检查，支持 Makefile、Go、Bun 和 npm 项目。
- `.github/workflows/pr-policy.yml`：运行原生 `git-governance` 门禁。
- `.github/scripts/validate_pr.py`：校验目标分支、分支名、PR 标题任务号和 PR 元数据。
- `.github/scripts/test_validate_pr.py`：治理校验器的单元测试。
- `.github/PULL_REQUEST_TEMPLATE.md`：开发 Agent 创建 PR 时使用的统一模板。
- `.github/CODEOWNERS`：为以后启用 Review 保留；初期不要求 Code Owner Review。

## 默认策略

- Required Checks：`ci`、`git-governance`。
- PR 标题：必须包含与正文元数据完全相同的完整 `task_id`。
- Review：通过 `review_policy.enabled: false` 关闭。
- 合并方式：Squash。

开发团队负责创建分支、Commit 和 PR。仓库内 GitHub Actions 负责原生门禁；接入外部 PR 检查 Agent 后，Agent 只检查状态、维护一条 PR 规范检查评论，并定向通知创建 PR 的开发 Agent。

从本模板创建仓库后，由 Git 治理管理员使用工具包中的 `bootstrap-repository.ps1` 配置分支保护。治理 Agent 不执行初始化。
