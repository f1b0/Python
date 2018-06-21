#!/bin/bash

osascript -e 'tell app "Terminal"
    do script "ssh _HOST_ -l _USERNAME_"
end tell'