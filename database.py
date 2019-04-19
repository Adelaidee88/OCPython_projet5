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
        self.fill_table()

    def connect_db(self):
        self.db = pymysql.connect(host="localhost", user="root",
                                  passwd="piO!u3Cui7", db="products")
        self.cur = self.db.cursor()

    def create_table(self, product_type):
        self.table = "CREATE TABLE IF NOT EXISTS " + product_type + \
                     "(" \
                "id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT," \
                "name VARCHAR(100) NOT NULL," \
                "nutriscore CHAR(1)," \
                "url VARCHAR(255)," \
                "labels TEXT," \
                "PRIMARY KEY (id))"
        self.cur.execute(self.table)

    def create_favorite(self):
        self.table = "CREATE TABLE IF NOT EXISTS favorites (" \
                     "id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, " \
                     "name VARCHAR(100) NOT NULL," \
                     "nutriscore CHAR(1)," \
                     "url VARCHAR(255)," \
                     "labels TEXT," \
                     "PRIMARY KEY (id))"
        self.cur.execute(self.table)

    def fill_table(self):
        base = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&" \
               "tagtype_0=categories&tag_contains_0=contains&tag_0="
        base2 = "&sort_by=unique_scans_n&page_size=20&axis_x=energy&axis_" \
                "y=products_n&action=display&json=1"
        list_products = {"pizza": base + "pizza" + base2,
                         "yaourt": base + "yogurt" + base2,
                         "pâte_à_tartiner": base + "fr:pates-a-tartiner" + base2,
                         "jambon": base + "white-hams" + base2,
                         "saucisse": base + "sausages" + base2,
                         "biscuit_au_chocolat": base + "chocolate-biscuits" + base2,
                         "légumes_préparés": base + "prepared-vegetables" + base2,
                         "soupe_de_légumes": base + "vegetable-soups" + base2,
                         }
        try:
            sql = "SELECT * FROM pizza;"
            self.cur.execute(sql)
        except:
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
                                "nutrition_grade_fr"] + '\"' + ", " \
                            + '\"' + response["products"][i]["url"] + '\"' + ", " \
                            + '\"' + response["products"][i][
                                "labels"] + '\"' + ")"
                    self.cur.execute(sql)
                except KeyError:
                    print("coucou")
                    pass
                    # sql = "INSERT INTO " + products + " VALUES (NULL, " \
                          # + '\"' + response["products"][i][
                          #     "product_name"] + '\"' + ", " \
                          # + '\"' + response["products"][i][
                          #     "nutrition_grade_fr"] + '\"' + ", " \
                          # + '\"' + response["products"][i]["url"] + '\"' + ", " \
                          # + "NULL)"
                    # self.cur.execute(sql)

    def get_category(self):
        sql = "SHOW TABLES WHERE tables_in_products != 'favorites';"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        list_category = []
        for row in rows:
            list_category.append(row)
        return list_category

    def get_aliments(self, category):
        sql = "SELECT name FROM " + category + ";"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        list_aliments = []
        for row in rows:
            list_aliments.append(row)
        return list_aliments

    def list_aliments(self, category):
        sql = "SELECT * FROM " + category + ";"
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
        print(choice[0])
        return choice[0]  # revoir formatage pour que ce soit joli

    def add_favorite(self, aliment, category):
        self.create_favorite()
        sql = "INSERT INTO favorites VALUES (NULL," + '\"' + str(aliment[1]) + '\"' \
              + ", " + '\"' + str(aliment[2]) + '\"' \
              + "," + '\"' + str(aliment[3]) + '\"' \
              + "," + '\"' + str(aliment[4]) + '\"' + ")"
        self.cur.execute(sql)
        self.db.commit()

    def show_favorites(self):
        sql = "SELECT * FROM favorites"
        self.cur.execute(sql)
        choice = self.cur.fetchall()
        print(choice)
        return choice

        # db = pymysql.connect(host="localhost", user="root",
        # passwd="piO!u3Cui7", db="test")
        # sql = "INSERT INTO test_table (description) VALUES (%s)"
        # val = ("patate")
        # cur.execute(sql, val)
        # db.commit()
# faire un test pour voir si tables existent avant de les remplir
# requête api pls pages et fix erreurs
