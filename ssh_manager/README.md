# A tkinter based ssh manager written in python3.6


Functionalities:
________________

  + read csv files as host list
  + opens a new terminal window which asks for login

Supported for:
______________

  + OSX
  + Linux (to do)

```bash
osascript -e 'tell app "Terminal"
    do script "ssh _HOST_ -l _USERNAME_"
end tell'
```
