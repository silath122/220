from sales_person import SalesPerson

class SalesForce:
    def __init__(self):
        sales_people = []
        self.sales_people = sales_people

    def add_data(self, file_name):
        self.file_name = file_name
        infile = open(self.file_name, 'r')
        for line in infile:
            self.sales_people.append(line)
        return self.sales_people

    def quota_report(self, quota):
        self.quota = quota
        employee_list = []

        # one line of data being split for an employee
        for employee in self.sales_people:
            employee_list.append(list(employee.split(' ')))







