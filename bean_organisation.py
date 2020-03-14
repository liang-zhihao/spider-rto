import my_db
class Organisation:
    def __init__(self):
        self.code=-1
        self.status = ""
        self.contact_name = ""
        self.job_title = ""
        self.organisation_name = ""
        self.email = ""
        self.address = ""

    def insert_into_table(self):
        sql = "insert into mytable\
        (code,status,contact_name,job_title,organisation_name,email,address) " \
              "values(?,?,?,?,?,?,?)"
        db = my_db.getDB()
        cur = db.cursor()
        cur.execute(sql, [self.code, self.status, self.contact_name, self.job_title,
                          self.organisation_name, self.email, self.address])
        db.commit()
        cur.close()
        db.close()

