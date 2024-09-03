## Basic Modes
```
Normal Mode: This is the default mode when you start vi. In this mode, you can navigate the file, delete text, copy and paste, etc.
Insert Mode: In this mode, you can insert and edit text. You can enter Insert Mode by pressing i, a, o, etc.
Command Mode: You access this mode from Normal Mode by pressing :. This mode allows you to execute commands like saving or quitting.
```

## Normal Mode to Insert Mode:
```
i - Insert before the cursor.
a - Insert after the cursor.
o - Open a new line below the current line and insert there.
I - Insert at the beginning of the line.
A - Insert at the end of the line.
gg: Go to the beginning of the file.
G: Go to the end of the file.
[line number]G: Go to a specific line number.
```

## Editing
```
x: Delete the character under the cursor.
dd: Delete the current line.
dw: Delete from the cursor to the end of the word.
d$: Delete from the cursor to the end of the line.
u: Undo the last change.
Ctrl + r: Redo the undone change.
yy: Copy (yank) the current line.
yw: Yank (copy) a word.
p: Paste the yanked or deleted text after the cursor.
P: Paste the yanked or deleted text before the cursor.
r: Replace the character under the cursor with another character.
```

## Saving and Quitting
```
:w: Save the file.
:wq or :x: Save and quit.
:q: Quit (only if no changes have been made).
:q!: Quit without saving changes.
:w [filename]: Save the file with a new name.
```

Note: /type - this helps to search the content "type" and once type and press enter and next press n to see how many other same content are present.