---
marp: true
theme: uncover
class: invert
paginate: false
title: Software design test presentation
author: Loïc Riegel
description: support for a training on how to improve the design of the software we produce.
---

# How to improve the design of you software?


---
### Error handling

---
###### Error handling :red_circle:

```Python
try:
    do_this()
    do_this()
    do_this()
    do_this_difficult_thing()
except:
    print("An error happened")
```

---

###### Error handling :white_check_mark:

```Python
class CustomException(Exception):
    """Custom exception that is raised when this happens"""

    def __init__(self, thing: str, msg: str | None):
        self.thing = thing
        self.msg = msg or "default message"
    
    def __str__(self) -> str:
        return self.msg

do_this()
do_this()
do_this()
try:
    do_this_difficult_thing()

except:
    print("An error happened")
```

---
###### Error handling :red_circle:
```Python
def main():
    try:
        my_var = float(input("Please enter a number: "))
        print(f"You entered {my_var}")

        whaterver
    except:
        pass
```

---
![](./assets/images/try-catch-with-name-error.png)

---
###### Error handling :white_check_mark:
```Python
    try:
        my_var = float(input("Please enter a number: "))
        print(f"You entered {my_var}")

    except ValueError:
        print("Please enter a valid number!")
```

---
###### Error handling
Keep exceptions at their level
See mermaid diagrams

---
###### Error handling
Keep exceptions at their level
```Python
class VacationDaysShortageError(Exception):
    """Custom error that is raised when not enough vacation days are available."""

    def __init__(self, requested_days: int, remaining_days: int, message: str) -> None:
        self.requested_days = requested_days
        self.remaining_days = remaining_days
        self.message = message
        super().__init__(message)
```

---
###### Error handling takeaways
- Don't silence exception
- Catch only specific exceptions
- Raise meaningful exceptions
- Use exception at their appropriate level, don't push low-level exception all the way to the top

---

