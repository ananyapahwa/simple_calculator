# Q1: Hands-On Guide to Creating and Resolving a Git Merge Conflict

This guide takes you through executing the entire workflow on your machine and GitHub, capturing screenshots, and completing your submission.

---

## 1. Local Repository Setup

Open your terminal and navigate to the project directory:

```bash
cd "/Users/ananya/Desktop/devops assignment/Q1_Git_Merge_Conflict"
```

Initialize the Git repository:

```bash
git init -b main
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

Add your initial files and commit:

```bash
git add calculator.py
git commit -m "Initial commit: Basic calculator functionality"
```

---

## 2. Link Local Repository to GitHub

1. Go to [GitHub](https://github.com) and click **New Repository**.
2. Name it: `cloud-devops-git-conflict-demo`.
3. Keep it **Public** (or Private), and **DO NOT** initialize with a README, .gitignore, or license.
4. Copy your repository's URL (e.g., `https://github.com/<your-username>/cloud-devops-git-conflict-demo.git`).
5. Run:

```bash
git remote add origin https://github.com/<your-username>/cloud-devops-git-conflict-demo.git
git push -u origin main
```

---

## 3. Creating Two Diverging Feature Branches

We will simulate two developers modifying the welcome banner function in `calculator.py` on line 20 concurrently.

### Branch A: `feature-banner-modern`
```bash
# Create and checkout branch A
git checkout -b feature-banner-modern

# Edit calculator.py: Change line 20 to:
# return "=== Welcome to Ultra Calculator Pro (v2.0 Modern) ==="
```

Commit the change on Branch A:
```bash
git add calculator.py
git commit -m "Update banner to modern branding in calculator.py"
git push -u origin feature-banner-modern
```

### Branch B: `feature-banner-minimal`
Now return to `main` and create Branch B:
```bash
git checkout main
git checkout -b feature-banner-minimal

# Edit calculator.py: Change line 20 to:
# return ">> Minimal Calculator CLI (v2.0 Fast) <<"
```

Commit the change on Branch B:
```bash
git add calculator.py
git commit -m "Update banner to minimal lightweight style"
git push -u origin feature-banner-minimal
```

---

## 4. Merging Branch A into `main` (Clean Merge)

Switch back to `main` and merge the first branch:

```bash
git checkout main
git merge feature-banner-modern
git push origin main
```
*Result:* Fast-forward (or clean three-way) merge. No conflict occurs here.

---

## 5. Merging Branch B into `main` (Triggering Intentional Conflict)

Now attempt to merge Branch B into `main`:

```bash
git merge feature-banner-minimal
```

### Expected Terminal Output:
```text
Auto-merging calculator.py
CONFLICT (content): Merge conflict in calculator.py
Automatic merge failed; fix conflicts and then commit the result.
```

📸 **Screenshot 1 to take here:**
Run:
```bash
git status
git diff
```
*Take a screenshot of the terminal showing `both modified: calculator.py` and the `<<<<<<< HEAD` conflict markers.*

---

## 6. Inspecting and Manually Resolving the Conflict

Open `calculator.py`. You will see Git's conflict markers:

```python
<<<<<<< HEAD
    return "=== Welcome to Ultra Calculator Pro (v2.0 Modern) ==="
=======
    return ">> Minimal Calculator CLI (v2.0 Fast) <<"
>>>>>>> feature-banner-minimal
```

### Resolution:
Edit `calculator.py` manually to reconcile both requirements (e.g. unified enterprise header):

```python
    # Resolved conflict: Clean unified banner incorporating modern identity
    return "=== Calculator CLI Pro v2.0 (Modern & Lightweight) ==="
```
*(Make sure to delete `<<<<<<< HEAD`, `=======`, and `>>>>>>> feature-banner-minimal`)*

---

## 7. Committing and Pushing the Resolved Merge

Stage the resolved file:
```bash
git add calculator.py
git status
```

📸 **Screenshot 2 to take here:**
*Take a screenshot showing `All conflicts fixed but you are still merging` / `Changes to be committed: modified: calculator.py`.*

Complete the merge commit:
```bash
git commit -m "Resolve merge conflict between feature-banner-modern and feature-banner-minimal"
git push origin main
```

📸 **Screenshot 3 to take here:**
Run:
```bash
git log --graph --oneline -n 6
```
*Take a screenshot of the commit graph showing the branch divergence and resolution merge commit.*
