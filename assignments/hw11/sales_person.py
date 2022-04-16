
class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        sales = []
        self.sales = sales

    def get_id(self):
        return int(self.employee_id)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        sum = 0.0
        for sale in self.sales:
            sum = sum + sale
        return sum

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if sum >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if self < other:
            return -1
        elif self > other:
            return 1
        else:
            return 0

    def __str__(self):
        return "employee_id-name: total sales"




