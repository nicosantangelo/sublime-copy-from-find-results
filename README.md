Sublime Copy from find in files
===============================

Little package to remove the line number when copying from the find in files panel

## Use

The command is designed to only work on the `Find Results` tab and just copy otherwise.

So you can just map it to the default copy action:

````javascript
// Linux or Windows
{ "keys": ["ctrl+c"], "command": "copy_from_find_in_files" }

// MacOS
{ "keys": ["super+c"], "command": "copy_from_find_in_files" }
````

If you don't like remapping, copy, just use `copy_from_find_in_files` on any keys you like.