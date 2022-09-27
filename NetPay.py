import EmployeeClass as ec
import PayrollDeductionClass as pd
from prettytable import PrettyTable


employee1 = ec.Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800)

charge1 = pd.Deduction('food court', '8/14/2022', 22.50, 39119)
charge2 = pd.Deduction('gift contribution', '8/12/2022', 25.00, 58475)
charge3 = pd.Deduction('food court', '8/17/2022', 15.25, 21547)
charge4 = pd.Deduction('vending machine', '8/22/2022', 3.00, 58475)
charge5 = pd.Deduction('vending machine', '8/5/2022', 2.75, 58475)

employeetable = PrettyTable()

employeetable.field_names = ['Name', 'ID Number', 'Department', 'Job Title', 'Monthly Salary']

employeetable.add_row([employee1.get_name(), employee1.get_id(), employee1.get_department(), employee1.get_job_title(), "${:0,.2f}".format(employee1.get_salary())])
print('Employee Table')
print(employeetable)
print()
print('Charge Table')
pdtable = PrettyTable()

pdtable.field_names = ['Description', 'Date', 'Charge', 'EmployeeID']
pdtable.add_row([charge1.get_description(), charge1.get_date(), charge1.get_charge(), charge1.get_empID()])
pdtable.add_row([charge2.get_description(), charge2.get_date(), charge2.get_charge(), charge2.get_empID()])
pdtable.add_row([charge3.get_description(), charge3.get_date(), charge3.get_charge(), charge3.get_empID()])
pdtable.add_row([charge4.get_description(), charge4.get_date(), charge4.get_charge(), charge4.get_empID()])
pdtable.add_row([charge5.get_description(), charge5.get_date(), charge5.get_charge(), charge5.get_empID()])

print(pdtable)
print()
print()
print('*** Employee Pay ***')
print('Name: ', employee1.get_name())
print('ID Number: ', employee1.get_id())
print('Department: ', employee1.get_department())
print('Gross Salary: ', "${:0,.2f}".format(employee1.get_salary()))

deducted_sal =  6800 - charge2.get_charge() - charge4.get_charge() - charge5.get_charge()

print("Net Pay ", "${:0,.2f}".format(deducted_sal))