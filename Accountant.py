class Accountant:
    def __init__(self, summary=0, income=0, outcome=0):
        self.__summary = summary
        self.__income = income
        self.__outcome = outcome

    def get_outcome(self):
        return self.__outcome

    def get_income(self):
        return self.__income

    def get_summary(self):
        return self.__summary

    def set_outcome(self, outcome):
        self.__outcome += outcome
        self.__summary -= outcome

    def set_income(self, income):
        self.__income += income
        self.__summary += income