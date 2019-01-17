import requests
import pymysql


tmp = pymysql.install_as_MySQLdb()
db = pymysql.connect(host="localhost", user="root", passwd="piO!u3Cui7",
                     db="products")
cur = db.cursor()

base_model = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=" + "jambons-blancs" + "&sort_by=unique_scans_n&page_size=10&axis_x=energy&axis_y=products_n&action=display&json=1"
print(base_model)
response = requests.get(base_model)
response = response.json()
print(response)

table = "CREATE TABLE IF NOT EXIST" + product_type + "(" \
        "id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT," \
        "name VARCHAR(40) NOT NULL," \
        "name_fr VARCHAR(40)," \
        "nutriscore CHAR(1)," \
        "url VARCHAR(100)," \
        "labels TEXT," \
        "PRIMARY KEY (id))"

sql = "INSERT INTO product_type VALUES (%s)"
val = ("patate")
cur.execute(sql, val)
db.commit()

# name = response["product"]["codes_tags"]
# print(name)
# nom : product_name_fr / product_name
# nutriscore : nutrition_grade_fr
# url : url
# description : labels
# attention car sur 1e page pête à tart, que du nutella
# pâtes à tartiner : https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=%22%20+%20%22pates-a-tartiner%22%20+%20%22&sort_by=unique_scans_n&page_size=10&axis_x=energy&axis_y=products_n&action=display&json=1
# pizza : https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=" + "pizzas" + "&sort_by=unique_scans_n&page_size=10&axis_x=energy&axis_y=products_n&action=display&json=1
# jambon blanc : https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=" + "jambons-blancs" + "&sort_by=unique_scans_n&page_size=10&axis_x=energy&axis_y=products_n&action=display&json=1
# yaourt : https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=%22%20+%20%22yaourts%22%20+%20%22&sort_by=unique_scans_n&page_size=10&axis_x=energy&axis_y=products_n&action=display&json=1
#

