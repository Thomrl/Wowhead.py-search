#! python3.5
#Search on wowhead from "run" (start + r)
import sys, webbrowser, pyperclip

#Get input from RUN (start + r)
sys.argv
print(sys.argv)

#Check length if only 1 paste whatever is in clipboard, else you've probably pasted it in or written something youself
if len(sys.argv) > 1:
    search = " ".join(sys.argv[1:]) #takes index 1 and after and put into search
else:
    search = pyperclip.paste() #puts whatever is in the clipboard into search

#opens the default browser, and searches on wowhead for the input
webbrowser.open("http://www.wowhead.com/search?q=" + search)
