class Employee:
    def __init__(self, name, id, department, job_title, salary):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__job_title = job_title
        self.__salary = salary

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def get_salary(self):
        return self.__salary
    
    