
# Challenge: My Cat Trashed My File!

## MISC: Vi Instructions

### Description

We are given two files:

- `cat.txt`
- `spaghetti.txt`

The file `cat.txt` contains a series of commands intended to be run inside the **vi editor** (or **vim**) on Linux systems.  
The idea is that `cat.txt` represents a sequence of automated keystrokes or edits that were "smashed" into the `spaghetti.txt` file.

Our task is to simulate or manually apply these commands to `spaghetti.txt` using `vi` to uncover the hidden flag.

### Solution

🧠 Step-by-step:

- Open `spaghetti.txt` in a `vi` editor.
- Replay or carefully interpret the commands in `cat.txt` as **vi editor operations**.
- These operations manipulate and clean up `spaghetti.txt` to reveal the flag.

After applying the vi keystrokes from `cat.txt`, the revealed flag is:

```
DawgCTF{pAwsibiLiti3s_ar3_m30wV3l0us}
```
