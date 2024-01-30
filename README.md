# CharByChar
---

- [Licence](https://github.com/Mechinsam/charByChar/blob/main/LICENCE)
- [Latest version](https://github.com/Mechinsam/charByChar/releases/tag/v1.1)

# About
Character by character is a python script allowing you to display text like this:

![ezgif com-gif-maker](https://user-images.githubusercontent.com/95701816/212156968-a233780f-4b51-4be5-bb15-ffdc6b569821.gif)

It works by printing one character than pausing for a short time then moving onto the next

```python   
    def line_print(self):
        to_print = ""
        for x in self.letters:
            sleep(self.delay)
            cs()
            to_print += x
           
            print(to_print)
```

# Installation

Open your prefered terminal (e.g. cmd, terminal. etc.)

Type:

```bash
pip install git+https://github.com/Mechinsam/charByChar.git
```
