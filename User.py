class user():
    def __init__(self,userid, fname, lname, dob, email, password, type):
        self.userid = userid
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.email = email
        self.password = password
        self.type = type

    def signin(self, userid, fname, lname, dob, email, password, type):
        self.userid = userid
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.email = email
        self.password = password
        self.type = type
    
    def signout(self):
        self.userid = None
        self.fname = None
        self.lname = None
        self.dob = None
        self.email = None
        self.password = None
        self.type = None