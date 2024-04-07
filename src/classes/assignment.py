from datetime import date


class Assignment:
    def __init__(self, assignment_date: date) -> None:
        self.__assignment_date: date = assignment_date

    def get_date(self) -> date:
        return self.__assignment_date
