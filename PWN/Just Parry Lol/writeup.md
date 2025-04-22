
# Challenge: Just Parry Lol

## PWN: Frame Data Manipulation

### Description

We are given a binary where we have to interact with a system involving "parrying" and "attacking".  
At first, the interactions seem limited, but further exploration hints at special powers being possible if we "feel faster" — suggesting that specific conditions or inputs unlock additional abilities.

### Solution

🧠 Step-by-step:

- Using the **Dogbolt Decompiler** ([dogbolt.org](https://dogbolt.org/)), we analyze the binary to better understand the logic.
- We discover that the player character can acquire a power-up called **"You Feel Faster"** if they use a **specific name**.
- The required name was found in the decompiled code:

```text
AUTOPARRY
```

- After setting the name to `AUTOPARRY`, we are able to perform double attacks using parry moves.

Specifically:

- Press `5` (parry)
- Press `5` again quickly (another parry)
- This triggers the hidden logic that reveals the flag.

Finally, the flag obtained is:

```
DawgCTF{fr4me_d4ta_m4nipulat10n}
```
