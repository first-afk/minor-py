# f = open('myProject2\\name.txt', 'r')


class Employee:
    def __init__(self, name, department, salary) -> None:
        self.name = name
        self.department = department
        self.salary = int(salary)

    def info(self):
        return f'The name of the worker is {self.name}, and is in {self.department} department, and they pay {self.salary} in that department'
    
    def __str__(self) -> str:
        return f'The name of the worker is {self.name}, and is in {self.department} department, and they pay {self.salary} in that department'



def employeedata(filename):
    employee = []
    with open(filename, 'r') as f:
        for name in f.readlines():
            employ = name.split(',')
            employee.append(Employee(employ[0], employ[1], employ[2]))
        return employee    

# for worker in employee:
#     print(f'{worker.name}, {worker.department}, {worker.salary}, ')


def main():
    totalsalary = 0
    staffdata = employeedata('myProject2\\name.txt')
    for data in staffdata:
        print(data)
        totalsalary += data.salary

    return totalsalary/len(staffdata)

print(main())