import datetime


class Students(object):
    sId = ""
    sName = ""
    sDoB = datetime
    sEmail = ""
    sPhone = ""
    sAddress = ""

    def __init__(self, s_id, s_name, s_dob, s_email, s_phone, s_address):
        self.sId = s_id
        self.sName = s_name
        self.sDoB = s_dob
        self.sEmail = s_email
        self.sPhone = s_phone
        self.sAddress = s_address
