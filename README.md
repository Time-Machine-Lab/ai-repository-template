# AI Repository Template

This template contains the minimum GitHub files for an AI-developed repository:

- .git-management.json: repository governance policy.
- .github/workflows/ci.yml: project checks.
- .github/workflows/pr-policy.yml: structured PR metadata check.
- .github/PULL_REQUEST_TEMPLATE.md: pull request contract.
- .github/CODEOWNERS: optional ownership rules.

The development agent creates branches and pull requests. The governance agent only observes pull requests and publishes the git-governance check.

After creating a repository from this template, apply branch protection with the bootstrap script from the Git governance package.
