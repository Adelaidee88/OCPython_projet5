import pymysql

tmp = pymysql.install_as_MySQLdb()
db = pymysql.connect(host="localhost", user="root", passwd="piO!u3Cui7",
                     db="products")
cur = db.cursor()
# cur.execute("SELECT * FROM test_table")
# for rows in cur.fetchall():
    # print(rows[0])
    # print(rows[1])
sql = "INSERT INTO test_table (description) VALUES (%s)"
val = ("patate")
cur.execute(sql, val)
db.commit()
for rows in cur.fetchall():
    print(rows[0])
    print(rows[1])
