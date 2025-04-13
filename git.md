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

List remote repos assiciated with local repo
```
git remote
git remove -v // include urls
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
force to accept self signed certificate
```
git -c http.sslVerify=false clone https://example.com/path/to/git
```
add "/home/project" to safe folder
```
git config --global --add safe.directory /home/project
```
## Drop changes
Rest changes in working directory
```
git rest
```
and discard all changes in working directory and reset repo to last commit
```
git reset -hard HEAD
```

Revert commit by applying new commit
```
git revert HEAD
```
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
