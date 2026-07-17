# Publish to GitHub

## Recommended visibility

Create this repository as **private**.

## GitHub CLI

From the parent directory of this folder:

```bash
gh repo create hbycwyh2008/NOAI-IOAI-Preparation-Curriculum --private --source ./NOAI-IOAI-Preparation-Curriculum --remote origin --push
```

If the remote repository already exists:

```bash
cd NOAI-IOAI-Preparation-Curriculum
git init
git add .
git commit -m "Initialize NOAI-IOAI-Preparation-Curriculum"
git branch -M main
git remote add origin https://github.com/hbycwyh2008/NOAI-IOAI-Preparation-Curriculum.git
git push -u origin main
```
