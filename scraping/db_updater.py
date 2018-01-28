import pymysql.cursors
import pymysql

with open("secrets.txt", "r") as secretfile:
    lines = secretfile.readlines()
    HOST = lines[0].rstrip()
    USER = lines[1].rstrip()
    PASSWORD = lines[2].rstrip()

# Connect to the database
connection = pymysql.connect(host=HOST,
                             user=USER,
                             password=PASSWORD,
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def create_tables():
    """
    Creates all tables in the DB
    """
    with connection.cursor() as cursor:
        create_items = "CREATE TABLE IF NOT EXISTS items(id int primary key, name varchar(32), vegetarian bool, vegan bool, gluten_free bool)"
        cursor.execute(create_items)
        create_eateries = "CREATE TABLE IF NOT EXISTS eateries(id int primary key, name varchar(32))"
        cursor.execute(create_eateries)
        create_stations = "CREATE TABLE IF NOT EXISTS stations(id int primary key, name varchar(32), eatery int, foreign key fk_eatery(eatery) references eateries(id) on update cascade on delete restrict)"
        cursor.execute(create_stations)
        create_eatery_hours = "CREATE TABLE IF NOT EXISTS eatery_hours(date varchar(32), daypart varchar(32), hours varchar(32), eatery int, foreign key fk_eatery(eatery) references eateries(id) on update cascade on delete restrict)"
        cursor.execute(create_eatery_hours)
        create_menus = "CREATE TABLE IF NOT EXISTS menus(item int, eatery int, station int, date varchar(32), daypart varchar(32), foreign key fk_eatery(eatery) references eateries(id) on update cascade on delete restrict, foreign key fk_item(item) references items(id) on update cascade on delete restrict, foreign key fk_station references stations(id) on update cascade on delete restrict)"
        cursor.execute(create_menus)

    connection.commit()


def process_response(obj):
    items = obj["items"]
    for day in obj["days"]:
        for cafe in day["cafes"]:
            # need to access 0th index of this list of lists (unsure why it's a list of lists)
            dayparts = cafe["dayparts"][0]
            name = cafe["name"]
            for part in dayparts:
                starttime = part["starttime"]
                endtime = part["endtime"]
                daypart = part["label"]
                stations = part["stations"]
                for station in stations:
                    station_name = station["label"]
                    station_id = station["id"]
                    station_items = station["items"]
                    for item_id in station_items:
                        # item is just the item id number
                        item_data = items[item_id]
                        options = item_data["cor_icon"]
                        item_name = item_data["label"]
                        vegetarian, vegan, gluten_free = extract_dietary_restrictions(options)


def extract_dietary_restrictions(restriction_arr):
    """"""
    vegetarian = False
    vegan = False
    gluten_free = False

    for restriction in restriction_arr:
        if "1" in restriction:
            vegetarian = True
        elif "4" in restriction:
            vegan = True
            vegetarian = True
        elif "9" in restriction:
            gluten_free = True

    return (vegetarian, vegan, gluten_free)


try:
    with connection.cursor() as cursor:
        # Create a new record
        delete = "DROP TABLE test"
        cursor.execute(delete)
        create = "CREATE TABLE IF NOT EXISTS test(id int primary key, data varchar(32))"
        cursor.execute(create)
        sql = "INSERT INTO `test` (`id`, `data`) VALUES (%s, %s)"
        cursor.execute(sql, (1, 'hi ryan'))

    create_tables()

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    #     cursor.execute(sql, ('webmaster@python.org',))
    #     result = cursor.fetchone()
    #     print(result)
finally:
    connection.close()
