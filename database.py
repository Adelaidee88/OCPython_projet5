import pymysql
import requests
import yaml
tmp = pymysql.install_as_MySQLdb()


class Database:
    """The database with the products"""

    def __init__(self):
        self.table = ""
        self.cur = None
        self.db = None
        self.connect_db()
        self.fill_table()

    def recup_info_connexion(self):
        with open("id_database.yml", 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return None

    def connect_db(self):
        info_connexion = self.recup_info_connexion()
        self.db = pymysql.connect(host=info_connexion["host"],
                                  user=info_connexion["user"],
                                  passwd=info_connexion["mdp"],
                                  db=info_connexion["db"])
        self.cur = self.db.cursor()

    def create_table(self):  
        self.table = "CREATE TABLE IF NOT EXISTS products (" \
                "id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT," \
                "name VARCHAR(100) NOT NULL," \
                "category VARCHAR(25)," \
                "store VARCHAR(255)," \
                "nutriscore CHAR(1)," \
                "url VARCHAR(255)," \
                "labels TEXT," \
                "PRIMARY KEY (id))"
        self.cur.execute(self.table)

    def create_favorite(self):  
        self.table = "CREATE TABLE IF NOT EXISTS favorites (" \
                     "id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, " \
                     "product SMALLINT UNSIGNED NOT NULL," \
                     "substitute SMALLINT UNSIGNED NOT NULL," \
                     "PRIMARY KEY (id))"
        fk_prod = "ALTER TABLE favorites ADD CONSTRAINT fk_prod_fav FOREIGN " \
                  "KEY (product) REFERENCES products(id)"
        fk_subs = "ALTER TABLE favorites ADD CONSTRAINT fk_subs_fav FOREIGN " \
                  "KEY (substitute) REFERENCES products(id)"
        self.cur.execute(self.table)
        self.db.commit()
        self.cur.execute(fk_prod)
        self.db.commit()
        self.cur.execute(fk_subs)
        self.db.commit()

    def fill_table(self):
        base = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&" \
               "tagtype_0=categories&tag_contains_0=contains&tag_0="
        base2 = "&sort_by=unique_scans_n&page_size=20&axis_x=energy&axis_" \
                "y=products_n&action=display&json=1"
        list_prod = {"pizza": base + "pizza" + base2,
                     "yaourt": base + "yogurt" + base2,
                     "pâte_à_tartiner": base + "fr:pates-a-tartiner" + base2,
                     "jambon": base + "white-hams" + base2,
                     "saucisse": base + "sausages" + base2,
                     "biscuit_au_chocolat": base + "chocolate-biscuits" + base2,
                     "légumes_préparés": base + "prepared-vegetables" + base2,
                     "soupe_de_légumes": base + "vegetable-soups" + base2,
                     }
        self.create_table()
        sql = "SELECT name FROM products WHERE id = 1"
        id_name = self.cur.execute(sql)
        if id_name == 0:
            self.fill_items(list_prod)
            self.db.commit()
            self.create_favorite()
            self.db.commit()
        else:
            pass

    def fill_items(self, list_products):
        for products, url in list_products.items():
            response = requests.get(url)
            response = response.json()
            for i in range(0, len(response["products"])):
                try:
                    sql = "INSERT INTO products VALUES (NULL, " \
                            + '\"' + response["products"][i][
                                  "product_name"] + '\"' + ',\"' \
                            + products + '\", ' \
                            + '\"' + str(response["products"][i]["stores_tags"]) + '\"' + ", " \
                            + '\"' + response["products"][i][
                                "nutrition_grade_fr"] + '\"' + ", " \
                            + '\"' + response["products"][i]["url"] + '\"' \
                            + ", " + '\"' + response["products"][i]["labels"] + '\"' + ")"
                    self.cur.execute(sql)
                except KeyError:
                    pass

    def get_category(self):
        sql = "SELECT DISTINCT category FROM products;"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        list_category = []
        for row in rows:
            list_category.append(row)
        return list_category

    def get_aliments(self, category):
        sql = "SELECT id, name FROM products WHERE category='" + category + "';"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        list_aliments = []
        for row in rows:
            list_aliments.append(row)
        return list_aliments

    def get_id_cat(self, category):
        sql = "SELECT id FROM products WHERE category='" + category + "';"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        list_id_cat = []
        for row in rows:
            list_id_cat.append(row)
        return list_id_cat

    def list_aliments(self, category):
        sql = "SELECT * FROM products WHERE category='" + category + "';"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        list_aliments = []
        for row in rows:
            list_aliments.append(row)
        return list_aliments

    def show_aliment(self, aliment, category):
        sql = "SELECT * FROM products WHERE category='" + \
              category + "' AND id = " + str(aliment) + ";"
        self.cur.execute(sql)
        choice = self.cur.fetchall()
        print("Votre choix : {} ayant {} comme nutriscore".format(choice[0][1],
                                                                  choice[0][4]))
        return choice[0]

    def add_favorite(self, product, subs):
        sql = "INSERT INTO favorites VALUES (NULL," + '\"' + str(product) \
              + '\"' + ", " + '\"' + str(subs) + '\"' + ")"
        self.cur.execute(sql)
        self.db.commit()

    def show_favorites(self):
        sql_fav = "SELECT * FROM favorites"
        self.cur.execute(sql_fav)
        list_fav = self.cur.fetchall()
        list_prod = []
        list_subs = []
        for i in range(0, len(list_fav)):
            sql_prod = "SELECT name FROM products WHERE id = " + \
                       str(list_fav[i][1]) + ";"
            self.cur.execute(sql_prod)
            prod = self.cur.fetchall()  
            list_prod.append(prod)
        for i in range(0, len(list_fav)):
            sql_subs = "SELECT * FROM products WHERE id = " + \
                       str(list_fav[i][2]) + ";"
            self.cur.execute(sql_subs)
            subs = self.cur.fetchall()   
            list_subs.append(subs)        
        choice = {}
        for i in range(0, len(list_prod)):
            choice[list_prod[i][0][0]] = list_subs[i][0]        
        return choice

    def my_aliment(self, id_alim):
        sql = "SELECT * from products WHERE id = " + str(id_alim)
        self.cur.execute(sql)
        choice = self.cur.fetchall()
        return choice[0]