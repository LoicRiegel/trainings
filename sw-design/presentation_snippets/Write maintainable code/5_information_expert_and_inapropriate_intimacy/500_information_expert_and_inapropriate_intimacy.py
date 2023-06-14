"""
Issue: inappropriate intimacy
Issue: not as close the data it needs! (cf information expert)
Fix: turn this method static or take it out of the class
"""

# BEFORE


class Day(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    ...
    SATURDAY = auto()
    SUNDAY = auto()

class Calendar:
    def __init__(self, year: int):
        self.year = year

    def add_event(self, event: Event) -> None:
        """Add a event to the calendar."""
        ...

    def update_event(self, event: Event) -> None:
        """Update an existing event of the calendar."""
        ...

    def delete_event(self, event: Event) -> None:
        """Delete an existing event from the calendar."""
        ...

    def is_weekend(self, day: Day) -> bool:
        """Return whether a day is a weekend day or not."""
        return day in (Day.SATURDAY, Day.SUNDAY)


# AFTER


class Day(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    ...
    SATURDAY = auto()
    SUNDAY = auto()

    def is_weekend(self) -> bool:
        return self in (self.SATURDAY, self.SUNDAY)


class Calendar:
    def __init__(self, year: int):
        self.year = year
        
    def add_event(self, event: Event) -> None:
        """Add a event to the calendar."""
        ...
    
    ...


# NOT IN SLIDES

"""Remark: we could also have created a pure function to do that:
"""
def is_weekend(day: Day) -> bool:
    return day in (Day.SATURDAY, Day.SUNDAY)

