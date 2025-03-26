import sys
import MySQLdb

#!/usr/bin/python3

if __name__ == "__main__":
    username, password, dbname, state_name = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    cur = db.cursor()
    query = """
    SELECT cities.name 
    FROM cities 
    JOIN states ON cities.state_id = states.id 
    WHERE states.name = %s 
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))
    cities = cur.fetchall()
    print(", ".join([city[0] for city in cities]))

    cur.close()
    db.close()