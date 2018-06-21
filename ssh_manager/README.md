# A tkinter based ssh manager written in python3.6


______________


Functionalities:


  + read csv files as host list
  + opens a new terminal window which asks for login


______________


Supported operating system:
  
  + OSX
  + Linux (to do)

Linux support can be done by editing both shell scripts.

```bash

# from:
osascript -e 'tell app "Terminal"
    do script "ssh _HOST_ -l _USERNAME_"
end tell'

# Linux example
xfce4-terminal -c "ls -la" --hold

```


