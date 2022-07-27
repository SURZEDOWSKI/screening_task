#I assume that the task is to create not "Employers" but "Employees", so i'll stick to that :>

list_of_employees=[]
list_of_departaments=[]

class Employee:
    def __init__(self, firstname, lastname, age, job, salary, bonus):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.job=job
        self.salary=salary
        self.bonus=bonus
        self.total_salary=salary+bonus
        #list_of_employees[str(len(list_of_employees)+1)]=self.firstname

    def applybonus(self, bonus):
        self.bonus=bonus
        self.total_salary=self.salary+bonus

    def emp_info(self):
        print("firstname: {}, lastname: {}, age: {}, job: {}, salary: {}, bonus: {}, total salary: {}".format(self.firstname, self.lastname, self.age, self.job, self.salary, self.bonus, self.total_salary))

    def export_emp_info_txt(self):
        with open('emp_info.txt','w') as f:
            f.write("firstname: {}, lastname: {}, age: {}, job: {}, salary: {}, bonus: {}, total salary: {}".format(self.firstname, self.lastname, self.age, self.job, self.salary, self.bonus, self.total_salary))


class Departament:
    def __init__(self, name, *users):
        self.name=name
        self.users=users

    def disp_emp(self):
        for i in range(len(self.users)):
            print(self.users[i].firstname, self.users[i].lastname, self.users[i].job)

    def disp_dep(self): #maybe im wrong but it doesnt make sense to me why sould anyone have method inside one Departament to display all Departaments
        print(list_of_departaments)

    def add_usr(self, *user):
        self.users+=user
        #print("Employees in {}: {}".format(self.name, self.users))

    def dep_info(self):
        print("name: {}".format(self.name))
        print("Employees:")
        self.disp_emp()

    def applybonus(self, bonus):
        for i in range(len(self.users)):
            self.users[i].bonus=bonus
            self.users[i].total_salary=self.users[i].total_salary+bonus
            print(self.users[i].firstname, self.users[i].lastname, self.users[i].bonus)

    def search_emp(self, name):
        for i in range(len(self.users)):
            if self.users[i].firstname == name or self.users[i].lastname == name:
                print("Found employee: ", self.users[i].firstname, self.users[i].lastname, self.users[i].job)


def emp_create(firstname, lastname, age, job, salary, bonus):

        list_of_employees.append(Employee(firstname, lastname, age, job, salary, bonus))
        list_of_employees[len(list_of_employees)-1].emp_info()


def emp_create_from_input():
    
    firstname=input("firstname: ")
    lastname=input("lastname: ")
    age=int(input("age: "))
    job=input("job: ")
    salary=int(input("salary: "))
    bonus=int(input("bonus: "))

    emp_create(firstname, lastname, age, job, salary, bonus)


def emp_remove(ID):
    list_of_employees.pop(ID)
    all_emp_info()
    print("ID's have been updated!!!")


def all_emp_info():
    ID = 0
    for i in list_of_employees:
        print("ID: "+str(ID))
        print(list_of_employees[ID].emp_info())
        ID+=1


def emp_apply_bonus(ID):
    list_of_employees[ID].applybonus(9999)
    print(list_of_employees[ID].firstname, list_of_employees[ID].bonus, list_of_employees[ID].total_salary)


def export_emp_info_txt(ID):
    list_of_employees[ID].export_emp_info_txt()


def dep_create(name, *users):

        list_of_departaments.append(Departament(name, *users))
        list_of_departaments[len(list_of_departaments)-1].disp_emp()


def dep_create_from_input():
    
    emp_id_list=[]

    name=input("name: ")
    usr_count = int(input("How many users do you want to add?: "))
    for i in range(usr_count):
        emp_id=input("employee's ID: ")
        emp_id_list.append(emp_id)

    list_of_departaments.append(Departament(name))
    for i in range(len(emp_id_list)):
        list_of_departaments[len(list_of_departaments)-1].add_usr(list_of_employees[i])


def all_dep_info():
    ID = 0
    for i in list_of_departaments:
        print("ID: "+str(ID))
        print(list_of_departaments[ID].dep_info())
        ID+=1


def dep_remove(ID):
    list_of_departaments.pop(ID)
    all_dep_info()
    print("ID's have been updated!!!")


def dep_apply_bonus(ID):
    list_of_departaments[ID].applybonus(int(input("Bonus amount: ")))


def search_emp_in_dep(dep_ID):
    name = input("Firstname or lastname os searched employee: ")
    list_of_departaments[dep_ID].search_emp(name)

def start():
    run = True
    while(run):
        print("********************\
        \nChoose action\
        \n1. Manage Employees \
        \n2. Manage Departaments \
        \nQ. EXIT\
        \n********************")   

        act = input()
        if act == "1":
            print("********************\
                \nChoose option: \
                \n1. Add employee \
                \n2. Remove employee  \
                \n3. Show all employees  \
                \n4. Apply bonus  \
                \n5. Export employee's info to .txt\
                \n********************")
            option = input()
            if option == "1":
                emp_create_from_input()
            elif option == "2":
                ID=int(input("Provide ID of employee to be deleted: "))
                emp_remove(ID)
            elif option == "3":
                all_emp_info()
            elif option == "4":
                ID=int(input("Provide ID of employee to be granted a bonus: "))
                emp_apply_bonus(ID)
            elif option == "5":
                ID=int(input("Provide ID of employee to export their data: "))
                export_emp_info_txt(ID)
            else:
                print("No such option available!")
        elif act == "2":
            print("********************\
                \nChoose option: \
                \n1. Add departament \
                \n2. Remove departament  \
                \n3. Show all departaments  \
                \n4. Apply bonus to departament's employees  \
                \n5. Search for employee by name\
                \n********************")
            option = input()
            if option == "1":
                dep_create_from_input()
            elif option == "2":
                ID=int(input("Provide ID of departament to be deleted: "))
                dep_remove(ID)
            elif option == "3":
                all_dep_info()
            elif option == "4":
                ID=int(input("Provide ID of departament whose employess will be granted a bonus: "))
                dep_apply_bonus(ID)
            elif option == "5":
                dep_ID=int(input("Provide ID of departament to be searched: "))
                search_emp_in_dep(dep_ID)
            else:
                print("No such option available!")
        elif act == "Q":
            run = False
        else:
            print("Podano złą wartość!")

start()
