from .integer import get_norm_form as get_norm_form_int


class DateHelp:
    DAY = 'День'
    WEEK = 'Неделя'
    MONTH = 'Месяц'
    YEAR = 'Год'

    def get_norm_form(self, count_day: int, period: str):
        if period == self.WEEK:
            return self.get_norm_form_week(count_day)
        if period == self.MONTH:
            return self.get_norm_form_month(count_day)
        if period == self.YEAR:
            return self.get_norm_form_year(count_day)
        return self.get_norm_form_day(count_day)

    def get_norm_form_calculate(self, count_day: int):
        if count_day < 7:
            return self.get_norm_form_day(count_day)
        elif count_day < 30:
            return self.get_norm_form_week(count_day // 7)
        elif count_day < 365:
            return self.get_norm_form_month(count_day // 30)
        return self.get_norm_form_year(count_day // 365)

    @staticmethod
    def get_norm_form_day(count_days: int):
        return get_norm_form_int(count_days, 'день', 'дня', 'дней')

    @staticmethod
    def get_norm_form_week(count_days: int):
        return get_norm_form_int(count_days, 'неделя', 'недели', 'недель')

    @staticmethod
    def get_norm_form_month(count_days: int):
        return get_norm_form_int(count_days, 'месяц', 'месяца', 'месяцев')

    @staticmethod
    def get_norm_form_year(count_days: int):
        return get_norm_form_int(count_days, 'год', 'года', 'лет')
