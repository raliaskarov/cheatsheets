# Basic git commands
Keyboard
Q: Quit pager
Spacebar: Scroll down one page.
Up/Down Arrow Keys: Scroll line by line.
G: Jump to the end of the output.
1G or gg: Jump to the beginning of the output.

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

Update changes
check for changes
```
git status
```
stage
```
git add .
```
commit
```
git commit -m "Your descriptive message about the updates"
```
push
```
git push
# or
git push origin main
```
