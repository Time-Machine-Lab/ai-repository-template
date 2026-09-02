# AI 项目仓库模板

本模板为 AI 开发项目提供最小化的 GitHub 治理基础。

## 文件说明

- `.git-management.json`：仓库治理策略，定义允许的分支格式、必需检查、审批数量和合并方式。
- `.github/workflows/ci.yml`：通用项目检查，支持 Makefile、Go、Bun 和 npm 项目。
- `.github/workflows/pr-policy.yml`：运行 `git-governance` 门禁。
- `.github/scripts/validate_pr.py`：校验目标分支、分支名和 PR 元数据。
- `.github/scripts/test_validate_pr.py`：治理校验器的单元测试。
- `.github/PULL_REQUEST_TEMPLATE.md`：开发 Agent 创建 PR 时使用的统一模板。
- `.github/CODEOWNERS`：项目关键路径的 Review 所有者配置。

## 使用边界

开发 Agent 负责创建分支、提交代码和创建 PR。仓库内 GitHub Actions 发布原生 `git-governance` 门禁；接入外部治理 Agent 后，由它只读观察 PR 并发布建议性的 `multica-governance` 检查。

从本模板创建仓库后，使用 Git 治理工具包中的 `bootstrap-repository.ps1` 配置分支保护。
