
# Screen Command Cheat Sheet

`screen` is a terminal multiplexer that allows you to manage multiple terminal sessions within a single window or SSH session. Below are the most commonly used `screen` commands.

---

## **Basic Commands**

### Start a New Screen Session
```bash
screen
```

### Start a Named Screen Session
```bash
screen -S session_name
```

---

## **Detaching and Reattaching**

### Detach from a Screen Session
Press:
```
Ctrl+A, then D
```

### List Active Screen Sessions
```bash
screen -ls
```

### Reattach to a Detached Screen Session
```bash
screen -r session_name_or_id
```

### Reattach to a Session (Force if Already Attached)
```bash
screen -dr session_name_or_id
```

---

## **Managing Sessions**

### Kill a Specific Screen Session
```bash
screen -X -S session_name_or_id quit
```

### Exit a Session (From Inside the Screen)
```bash
exit
```

---

## **Window Management**

### Create a New Window Inside a Screen Session
Press:
```
Ctrl+A, then C
```

### Switch Between Windows
Press:
```
Ctrl+A, then N  # Next window
Ctrl+A, then P  # Previous window
```

### Close a Window
Press:
```
Ctrl+A, then K
```

---

## **Advanced Features**

### Split the Screen Horizontally
Press:
```
Ctrl+A, then S
```

### Switch to a Split Pane
Press:
```
Ctrl+A, then Tab
```

### Close a Split Pane
Press:
```
Ctrl+A, then X
```

---

## **Logging**

### Enable Logging for a Screen Session
Start the screen session with logging enabled:
```bash
screen -L
```

Logs are saved as `screenlog.0` in the current directory.

---

## **Examples**

### Run a Command in a New Screen Session
```bash
screen -S my_session_name command_to_run
```

### Run a Long-Running Process
```bash
screen -S long_process
# Run your process
Ctrl+A, then D  # Detach
screen -r long_process  # Reattach later
```

---

## **Quick Shortcuts**

| Shortcut         | Description                     |
|------------------|---------------------------------|
| `Ctrl+A, then D` | Detach from session            |
| `Ctrl+A, then C` | Create a new window            |
| `Ctrl+A, then N` | Switch to the next window      |
| `Ctrl+A, then P` | Switch to the previous window  |
| `Ctrl+A, then K` | Kill the current window        |
| `Ctrl+A, then S` | Split the screen horizontally  |
| `Ctrl+A, then X` | Close a split pane             |
| `Ctrl+A, then Tab` | Switch to another pane       |

---

Save this file and upload it to GitHub as a reference for managing `screen` sessions. Let me know if you need further help!
