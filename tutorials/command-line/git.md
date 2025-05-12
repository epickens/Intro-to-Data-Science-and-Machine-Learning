# Git Tutorial

## Basic Git Commands

### `git clone`

**Git clone** creates a local copy of a remote repository on your computer. This command downloads all files, branches, and commit history.

**Example:**

```bash
# Clone a repository from GitHub
git clone https://github.com/username/repository.git

# Clone to a specific folder
git clone https://github.com/username/repository.git my-project-folder
```

### `git add`

**Git add** stages changes for the next commit. It tells Git which files you want to include in your next commit.

**Example:**

```bash
# Add a specific file
git add filename.py

# Add all files in the current directory
git add .

# Add all files with a specific extension
git add *.csv
```

### `git commit`

**Git commit** saves your staged changes to the local repository with a descriptive message explaining what changes were made.

**Example:**

```bash
# Commit with a message
git commit -m "Add data preprocessing function"

# Add and commit in one command (only works for tracked files)
git commit -am "Fix bug in visualization code"
```

### `git push`

**Git push** uploads your local commits to a remote repository, making your changes available to others.

**Example:**

```bash
# Push to the default remote (origin) and branch
git push

# Push to a specific remote and branch
git push origin main

# Push a local branch to a remote repository for the first time
git push -u origin new-feature
```

For most basic tasks, `git push` is all you need.

### `git merge`

**Git merge** combines changes from different branches. It integrates the changes from a specified branch into your current branch.

**Example:**

```bash
# Merge a feature branch into your current branch
git merge feature-branch

# Merge with a commit message
git merge feature-branch -m "Merge feature X into main"
```

## Working With Forked Repositories

### Checking/Adding Remote Sources

**Remote sources** are connections to other repositories. When working with forks, you'll typically have your fork as `origin` and the original repository as `upstream`.

**Example:**

```bash
# List existing remotes
git remote -v

# Add the original repository as upstream
git remote add upstream https://github.com/original-owner/original-repository.git

# Verify the new remote
git remote -v
```

### `git fetch`

**Git fetch** downloads changes from a remote repository without merging them into your working files. This is useful to see what others have been working on.

**Example:**

```bash
# Fetch from origin
git fetch origin

# Fetch from upstream
git fetch upstream

# Fetch all remotes
git fetch --all
```

### `git merge upstream/main`

This command **merges changes from the upstream's main branch** into your current branch, keeping your commit history.

**Example:**

```bash
# First fetch the latest from upstream
git fetch upstream

# Then merge upstream changes into your current branch
git merge upstream/main
```

If you are working with a forked repository, this will help you stay up to date with the original repo.

### `git rebase upstream/main`

**Git rebase** rewrites your commit history by placing your commits on top of the upstream changes. This creates a cleaner, linear history compared to merging.

**Example:**

```bash
# First fetch the latest from upstream
git fetch upstream

# Then rebase your changes on top of upstream
git rebase upstream/main
```

## Working With Branches

### `git checkout`

**Git checkout** switches between branches or creates new branches. It's how you navigate your repository's different lines (branches) of development.

**Example:**

```bash
# Switch to an existing branch
git checkout feature-branch

# Create and switch to a new branch
git checkout -b new-feature

# Checkout a specific commit (detached HEAD state)
git checkout a1b2c3d4

# Discard changes in a file
git checkout -- filename.py
```

## Going Back in Time

### `git reset`

**Git reset** moves the current branch pointer to a specified commit, effectively "undoing" commits. How it affects your working directory depends on the mode used.

**Example:**

```bash
# Reset to a specific commit
git reset a1b2c3d4

# Reset to the previous commit
git reset HEAD~1
```

#### `--soft`

**Soft reset** moves the branch pointer but keeps your changes staged. This is useful when you want to recommit with different changes.

**Example:**

```bash
# Undo the last commit but keep changes staged
git reset --soft HEAD~1
```

#### `--hard`

**Hard reset** moves the branch pointer and discards all changes, reverting your working directory to the specified commit. **This permanently removes uncommitted changes.**

**Example:**

```bash
# Completely discard the last commit and all changes
git reset --hard HEAD~1

# Reset to a specific commit, discarding all subsequent changes
git reset --hard a1b2c3d4
```

Generally speaking, you **should not** do hard resets. Be very careful when using this flag.
