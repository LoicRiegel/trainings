# Before

class Employee:
    ...

    def take_a_holiday(self, payout: bool, nr_days: int = 1) -> None:
        if payout:
            if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
                raise ValueError(
                    f"You don't have enough holidays left over for a payout.\
                        Remaining holidays: {self.vacation_days}."
                )
            self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
            print(f"Paying out a holiday. Holidays left: {self.vacation_days}")
        else:
            if self.vacation_days < nr_days:
                raise ValueError(
                    "You don't have any holidays left."
                )
            self.vacation_days -= nr_days

# After

class Employee:
    ...

    def payout_holiday(self) -> None:
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise ValueError(
                f"You don't have enough holidays left over for a payout.\
                    Remaining holidays: {self.vacation_days}."
            )
        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out a holiday. Holidays left: {self.vacation_days}")

    def take_holiday(self, nr_days: int = 1) -> None:
        if self.vacation_days < nr_days:
            raise ValueError("You don't have any holidays left.")
        self.vacation_days -= nr_days