import pymysql
tmp = pymysql.install_as_MySQLdb()


class Database:
    """The database with the products"""

    def __init__(self, name):
        self.name = name

    # def connect_db(self):

    def create_table(self, product_type):
        table = "CREATE TABLE IF NOT EXIST" + '\"' + product_type + '\"' + "(" \
                "id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT," \
                "name VARCHAR(40) NOT NULL," \
                "name_fr VARCHAR(40)," \
                "nutriscore CHAR(1)," \
                "url VARCHAR(100)," \
                "labels TEXT," \
                "PRIMARY KEY (id))"

    # def create_favorite(self):

    # def fill_table(self, ):

        # db = pymysql.connect(host="localhost", user="root", passwd="piO!u3Cui7",
                             # db="test")
        # sql = "INSERT INTO test_table (description) VALUES (%s)"
        # val = ("patate")
        # cur.execute(sql, val)
        # db.commit()
