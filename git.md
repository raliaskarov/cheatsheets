# Basic git commands
## Keyboard
Q: Quit pager
Spacebar: Scroll down one page.
Up/Down Arrow Keys: Scroll line by line.
G: Jump to the end of the output.
1G or gg: Jump to the beginning of the output.

## Config 
Check which account
```
git config user.name
git config user.email

git config --global user.name
git config --global user.email

```
Clear credentials memory
```
git credential-cache exit
```
Unlink gihub repo 
```
git remote remove origin
```
Link to new github repo
```
git remote add origin https://github.com/<your-username>/<new-repository-name>.git
```

or to use ssh
if no remote set yet
```
git remote add origin git@github.com:yourusername/yourrepo.git
```

if remote exists
for ssh:
```
git remote set-url origin git@github.com:yourusername/yourrepo.git
```
for pat:
```
git remote set-url origin https://github.com/username/repo.git
```

List remote repos assiciated with local repo
```
git remote
git remove -v // include urls
```

set upstream branch
```
git push --set-upstream origin bug-fix-typo
```

## Update changes
check for changes
```
git status
```
stage (from current directory)
```
git add .
```
stage (regardless from where you are in the tree)
```
git add -A
```
commit
```
git commit -m "Your descriptive message about the updates"
```
set branch
```
git branch -M main
```
push
```
git push
# or
git push origin main
```

Push and overwrite remote 
```
git push -u origin master --force
```

NOT RECOMMENDED! force to accept self signed certificate
```
git -c http.sslVerify=false clone https://example.com/path/to/git
```
add "/home/project" to safe folder
```
git config --global --add safe.directory /home/project
```

## Puling from branch while already changed the file
```
# 1. Save your current changes temporarily
git stash

# 2. Switch to your teammate’s branch
git checkout additional_tests

# 3. Apply your saved changes to this branch
git stash pop
```

## Drop changes
Reset changes in working directory
```
git reset
git rest origin/main # --> use this 
```
and discard all changes in working directory and reset repo to last commit
```
git reset -hard HEAD
```

Rest in soft way - unstage but keep locall changes
```
git reset --soft HEAD~1
# unstage the heavy file
git reset bigfile.ext

# remove it from git tracking
git rm --cached bigfile.ext

# commit again
git add .
git commit -m "commit without large file"
```


Revert commit by applying new commit - this will remove local files and changes!
```
git revert HEAD
```

## Merge changes
Just to see where you stand
```
git status
```

Show commits that are on remote but not in your local main
```
git log --oneline --graph --decorate main..origin/main
```

Show commits that are on your local main but not on remote
```
git log --oneline --graph --decorate origin/main..main
```

Merge and keep full history
```
git pull --no-rebase origin main
```


### If git add . with untintended content 
clear index
```
git rm -r --cached .
```

add gitignore and add only it
```
git add .gitignore
git commit -m "Ensure .gitignore is correct"
```

remove everything from index
```
git rm -r --cached .
```

add all again
```
git add .
```

remove 

## Manage repo
### Rename repo

Rename origin into upstream
```
git remote rename origin upstream
```

Remove repo
```
git remote rm origin
```

Generate patches for email submission
Create patches for the last three commits
```
git format-patch HEAD~3
```

## Branches
```
git branch // list branches
git branch <new-branch> // create new branch
git branch -d <branch-name> // delete branch
git push origin --delete master // delete branch in remote
```

After creating new branch push it to remote
```
git push -u origin <new-branch-name>
```

View remote branches
```
git branch -r
```

Switch to main branch
```
git checkout main
```

Create branch and switch into it
```
git checkout -b my1stbranch
```

Clone
```
git clone <repo URL>
```

Pull latest version from remote
```
git pull origin master
git pull origin main
```

Pull an overwrite local changed

Download commits from remote 
```
git fetch origin
```
```git fetch --all --prune``` to download all and stop tracking merged branches

Reset local to remote, overwrite all local
```
git reset --hard origin/master
```

### When working on a new feature on a new branch
```
git checkout main
git pull
git checkout -b task3.2_some_new_feature
git add .
git commit -m "Implement new feature"
git push -u origin task3.2_some_new_feature
```

## Pull request
Generate summary of pending changes 
```
git request-pull origin/main <myfork or branch_name>
```

Send a collection of patches as emails
```
git send-email *.patch
```

Apply patchesto the repository
```
git am <patchfile.patch>
```


## Other
```
git version // version of git installed to system
```

get difference
```
git diff (diff vs last commit)
git diff HEAD~1 GEAD (last vs second last)
git diff <branch-1> <branch-2> (compare specific branches)
```

**git daemon**
Expose repositories via the Git:// protocol. The Git protocol is a lightweight protocol designed for efficient communication between Git clients and servers.
```
git daemon –base-path=/path/to/repositories
```

**instaweb**
Instantly launch a web server to browse repositories. It provides a simplified way to view repository contents through a web interface without the need for configuring a full web server.
```
git instaweb –httpd=webrick
```

**rerere**
Reuse recorded resolution of previously resolved merge conflicts. 
 - rerere.enabled configuration option needs to be set to "true" (git config –global rerere.enabled true) for git rerere to work. 
 - git rerere only applies to conflicts that have been resolved using the same branch and commit.
```
git rerere
```

## Use ssh
After you generated key pair and uploaded public key to GH

check key is in place
```
ls ~/.ssh/
```

See if remote is using HTTPs
```
git remote -v
```
if response looks like

origin  git@github.com:yourusername/yourrepo.git (fetch)
origin  git@github.com:yourusername/yourrepo.git (push)


then switch to ssh:
```
git remote set-url origin git@github.com:yourusername/yourrepo.git
```

Test
```
ssh -T git@github.com
```

Should give: "Hi yourusername! You've successfully authenticated, but GitHub does not provide shell access."

