to backup folder (Windows)
```
@echo off
SET source="D:\source_directory"
SET destination="E:\destination_directory"
SET log_file="E:\backup_log.txt"

robocopy "D:" "E" /MIR /XO /Z /TEE /ETA /LOG:"E:\backup_log.txt"

```
Options:
- /S - Copies subdirectories, but not empty ones.
- /E - Copies directories and subdirectories, including empty ones.
- /COPY - Specifies the file properties to be copied. You can use the following parameters with /COPY: D (Data), A (Attributes), T (Timestamps), S (Security), O (Owner information), U (Auditing information).
- /PURGE - Deletes destination files and directories that no longer exist in the source.
- /MIR - Mirrors a directory tree (equivalent to /E plus /PURGE).
- /FFT - Uses FAT file timing instead of NTFS.
- /Z - Copies files in restartable mode.
- /LOG - Writes the status output to the log file.
- /R - Specifies the number of retries on failed copies (default is 1 million).
- /W - Specifies the wait time between retries (default is 30 seconds).
- /MT - Enables multi-threaded copying with N threads (default is 8).
- /XC - Excludes changed files.
- /XN - Excludes newer files.
- /XO - Excludes older files. Will copy files which were updated.
- /L - Displays files that would be copied or deleted without actually performing the operation.
- /NP - Specifies that the progress of the copying operation will not be displayed.
- /IPG - Specifies the inter-packet gap to free bandwidth on slow lines.
- /TEE option displays the output in the console window.
- /ETA option provides an estimated time of arrival.
