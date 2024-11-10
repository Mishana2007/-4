class InputData:
    def __init__(self, car_model, owner, entry_time):
        self.car_model = car_model
        self.owner = owner
        self.entry_time = entry_time

class TimeTracking:
    def __init__(self, entry_time):
        self.entry_time = entry_time
        self.exit_time = None

    def calculate_duration(self):
        # Реализация вычисления времени пребывания
        pass

class Billing:
    def __init__(self, base_rate, discounts):
        self.base_rate = base_rate
        self.discounts = discounts

    def calculate_cost(self, duration):
        # Реализация расчета стоимости с учетом скидок и задолженностей
        pass

class Report:
    def generate_report(self, data):
        # Вывод информации о текущей задолженности и скидках
        pass
