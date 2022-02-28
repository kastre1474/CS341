class user():
    def __init__(self, fname, lname, dob, email, password, type, userid):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.email = email
        self.password = password
        self.type = type
        self.userid = userid
    
    def signin(self, fname, lname, dob, email, password, type, userid):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.email = email
        self.password = password
        self.type = type
        self.userid = userid
    
    def signout(self):
        self.fname = None
        self.lname = None
        self.dob = None
        self.email = None
        self.password = None
        self.type = None
        self.userid = None