import pymysql
import requests
tmp = pymysql.install_as_MySQLdb()


class Database:
    """The database with the products"""

    def __init__(self):
        self.table = ""
        self.cur = None
        self.db = None
        self.connect_db()

    def connect_db(self):
        self.db = pymysql.connect(host="localhost", user="root",
                                  passwd="piO!u3Cui7", db="products")
        self.cur = self.db.cursor()

    def create_table(self, product_type):
        self.table = "CREATE TABLE IF NOT EXIST" + '\"' + product_type + '\"' +\
                     "(" \
                "id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT," \
                "name VARCHAR(100) NOT NULL," \
                "name_fr VARCHAR(100)," \
                "nutriscore CHAR(1)," \
                "url VARCHAR(255)," \
                "labels TEXT," \
                "PRIMARY KEY (id))"
        self.cur.execute(self.table)

    # def create_favorite(self):

    def fill_table(self):
        base = "https://fr-en.openfoodfacts.org/category/"
        list_products = {"pizza": base + "pizzas/1.json",
                         "yaourt": base + "yogurts.json",
                         "pâte_à_tartiner": base + "fr:pates-a-tartiner/2.json",
                         "jambon": base + "white-hams.json"}
        for products in list_products.keys():
            self.create_table(products)
        self.fill_items(list_products)
        self.db.commit()

    def fill_items(self, list_products):
        for products, url in list_products.items():
            response = requests.get(url)
            response = response.json()
            for i in range(0, len(response)):
                try:
                    sql = "INSERT INTO " + products + " VALUES (NULL, " \
                          + '\"' + response["products"][i][
                              "product_name"] + '\"' + ", " \
                          + '\"' + response["products"][i][
                              "product_name_fr"] + '\"' + ", " \
                          + '\"' + response["products"][i][
                              "nutrition_grade_fr"] + '\"' + ", " \
                          + '\"' + response["products"][i]["url"] + '\"' + ", " \
                          + '\"' + response["products"][i][
                              "labels"] + '\"' + ")"
                    self.cur.execute(sql)
                except KeyError:
                    sql = "INSERT INTO " + products + " VALUES (NULL, " \
                          + '\"' + response["products"][i][
                              "product_name"] + '\"' + ", " \
                          + '\"' + response["products"][i][
                              "product_name_fr"] + '\"' + ", " \
                          + '\"' + response["products"][i][
                              "nutrition_grade_fr"] + '\"' + ", " \
                          + '\"' + response["products"][i]["url"] + '\"' + ", " \
                          + "NULL)"
                    self.cur.execute(sql)

    def get_category(self):
        sql = "SHOW TABLES;"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        list_category = []
        for row in rows:
            list_category.append(row)
        return list_category

    def get_aliments(self, category):
        sql = "SELECT name_fr FROM " + category + ";"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        list_aliments = []
        for row in rows:
            list_aliments.append(row)
        return list_aliments

    def show_aliment(self, aliment, category):
        sql = "SELECT * FROM " + category + " WHERE id = " + str(aliment) + ";"
        self.cur.execute(sql)
        choice = self.cur.fetchall()
        print(choice[0])  # revoir formatage pour que ce soit joli

        # db = pymysql.connect(host="localhost", user="root",
    # passwd="piO!u3Cui7", db="test")
        # sql = "INSERT INTO test_table (description) VALUES (%s)"
        # val = ("patate")
        # cur.execute(sql, val)
        # db.commit()
