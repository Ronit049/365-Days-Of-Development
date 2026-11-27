# 🌿 Git and GitHub Workflow

## Start a repository

```bash
git init
git status
git add README.md
git commit -m "docs: add project readme"
```

## Everyday commands

```bash
git status
git add .
git commit -m "feat: add login form"
git log --oneline
git pull
git push
```

## Branch workflow

```bash
git switch -c feature/profile-page
# Make and test changes
git add .
git commit -m "feat: add profile page"
git push -u origin feature/profile-page
```

Open a pull request on GitHub and describe the change and how it was tested.

## Useful commit prefixes
- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation
- `refactor:` code restructuring without intended behavior change
- `test:` tests
- `chore:` maintenance

## Good habits
- Commit related changes together.
- Write messages that explain the change.
- Do not commit passwords, API keys, tokens, or private data.
- Use `.gitignore` for generated files and local environments.
- Review `git diff` before committing.

Resource: [Git documentation](https://git-scm.com/doc)
