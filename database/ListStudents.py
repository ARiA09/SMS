from model.Students import Students

import datetime


class ListStudent(object):
    listStudent = [Students("S01", "Nguyen Van A", datetime.date(1990, 3, 12), "A@email", "123456789", "District 10"),
                   Students("S02", "Nguyen Van B", datetime.date(1991, 3, 12), "A@email", "123456789", "District 10")]

    @classmethod
    def add_to_list(cls):
        s_id = input("Type Student ID:\n")
        for i, x in enumerate(cls.listStudent):
            if s_id in x.sId:
                print("Student ID " + s_id + " already exist!!!")
                return

        s_name = input("Type Student Name:\n")
        s_dob = None
        while s_dob is None:
            input_dob = input("Type Student DOB(YYYY-MM-DD):\n")
            try:
                year, month, day = map(int, input_dob.split('-'))
                s_dob = datetime.date(year, month, day)
            except ValueError:
                print("Incorrect format(YYYY-MM-DD format)")
                pass

        s_email = input("Type Student Email:\n")
        s_phone = input("Type Student Phone:\n")
        s_address = input("Type Student Address:\n")

        a_student = Students(s_id, s_name, s_dob, s_email, s_phone, s_address)

        cls.listStudent.append(a_student)

    @classmethod
    def update_student(cls):
        index_student = 0
        check_exist = 'false'
        update_student = Students
        s_id = input("Type Student ID:\n")

        for i, x in enumerate(cls.listStudent):
            if s_id in x.sId:
                index_student = i
                update_student = x
                check_exist = 'true'
                break

        if check_exist == 'true':
            print("Student ID: " + update_student.sId
                  + "\nPlease input if you want to update or Enter to keep the recode")
            us_id = input("Type Student ID:\n")

            print("Student Name: " + update_student.sName
                  + "\nPlease input if you want to update or Enter to keep the recode")
            us_name = input("Type Student Name:\n")

            print("Student DOB: " + update_student.sDoB.strftime('%m/%d/%Y')
                  + "\nPlease input if you want to update or Enter to keep the recode")
            while True:
                input_dob = input("Type Student DOB(YYYY-MM-DD format):\n")
                if len(input_dob) > 0:
                    try:
                        year, month, day = map(int, input_dob.split('-'))
                        us_dob = datetime.date(year, month, day)
                    except ValueError:
                        print("Incorrect format(YYYY-MM-DD format)")
                        continue
                    else:
                        break

            print("Student Email: " + update_student.sEmail
                  + "\nPlease input if you want to update or Enter to keep the recode")
            us_email = input("Type Student Email:\n")

            print("Student Phone: " + update_student.sPhone
                  + "\nPlease input if you want to update or Enter to keep the recode")
            us_phone = input("Type Student Phone:\n")

            print("Student Address: " + update_student.sAddress
                  + "\nPlease input if you want to update or Enter to keep the recode")
            us_address = input("Type Student Address:\n")

            if len(us_id) <= 0:
                us_id = update_student.sId

            if len(us_name) <= 0:
                us_name = update_student.sName

            if len(input_dob) <= 0:
                us_dob = update_student.sDoB

            if len(us_email) <= 0:
                us_email = update_student.sEmail

            if len(us_phone) <= 0:
                us_phone = update_student.sPhone

            if len(us_address) <= 0:
                us_address = update_student.sAddress

            update_student = Students(us_id, us_name, us_dob, us_email, us_phone, us_address)

            cls.listStudent[index_student] = update_student

        if check_exist == 'false':
            print("Student ID " + s_id + " doesn't exist!!!")

    @classmethod
    def delete_student(cls):
        check_exist = 'false'
        s_id = input("Type Student ID:\n")

        for i, x in enumerate(cls.listStudent):
            if s_id in x.sId:
                cls.listStudent.remove(x)
                print("Student ID " + s_id + " has removed!!!")
                check_exist = 'true'
                break
        if check_exist == 'false':
            print("Student ID " + s_id + " doesn't exist!!!")

    @classmethod
    def search_student(cls):
        check_exist = 'false'
        s_name = input("Type Student Name: ")
        for i, x in enumerate(cls.listStudent):
            if s_name not in x.sName:
                continue
            else:
                check_exist = 'true'
                print("Student ID: " + x.sId +
                      "\nStudent Name: " + x.sName +
                      "\nStudent DOB: " + x.sDoB.strftime('%m/%d/%Y') +
                      "\nStudent Email: " + x.sEmail +
                      "\nStudent Phone: " + x.sPhone +
                      "\nStudent Address: " + x.sAddress +
                      "\n----------------------------------")
        if check_exist == 'false':
            print("Not Found!!!")

    @classmethod
    def print_out_list(cls):
        for x in cls.listStudent:
            print("Student ID: " + x.sId +
                  "\nStudent Name: " + x.sName +
                  "\nStudent DOB: " + x.sDoB.strftime('%m/%d/%Y') +
                  "\nStudent Email: " + x.sEmail +
                  "\nStudent Phone: " + x.sPhone +
                  "\nStudent Address: " + x.sAddress +
                  "\n----------------------------------")
