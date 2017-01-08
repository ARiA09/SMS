from database.ListStudents import ListStudent


class Main:
    if __name__ == '__main__':
        print('This program is being run by itself')
    else:
        print('I am being imported from another module')

    while 1:
        command = input("What do you want to do?\nA=Add \nU=Update \nD=Delete \nV=View \nS=Search \nE=Exit \n")
        if command == "A":
            ListStudent.add_to_list()
            ListStudent.print_out_list()
        if command == "U":
            ListStudent.update_student()
            ListStudent.print_out_list()
        if command == "D":
            ListStudent.delete_student()
            ListStudent.print_out_list()
        if command == "V":
            ListStudent.print_out_list()
        if command == "S":
            ListStudent.search_student()
        if command == "E":
            exit()
