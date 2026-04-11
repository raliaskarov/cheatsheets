
# Mount cloud storage
```
sudo pacman -S rclone
rclone config  # follow prompts to authorize Google Drive
rclone sync gdrive:/ /your/hard/drive/
```
