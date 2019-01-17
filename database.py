import pymysql
tmp = pymysql.install_as_MySQLdb()


class Database:
    """The database with the products"""

    def __init__(self, name):
        self.name = name

    # def create_table(self):

    # def create_favotite(self):

    # def fill_table(self):

        # db = pymysql.connect(host="localhost", user="root", passwd="piO!u3Cui7",
                             # db="test")
        # sql = "INSERT INTO test_table (description) VALUES (%s)"
        # val = ("patate")
        # cur.execute(sql, val)
        # db.commit()
