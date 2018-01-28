import pymysql.cursors
import pymysql
import os
import json

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


sql = "INSERT INTO `test` (`id`, `data`) VALUES (%s, %s)"
insert_items = "INSERT IGNORE INTO `items` (`id`, `name`, `vegetarian`, `vegan`, `gluten_free`) VALUES (%s, %s, %s, %s, %s)"
insert_eateries = "INSERT IGNORE INTO `eateries` (`id`, `name`) VALUES (%s, %s)"
insert_stations = "INSERT IGNORE INTO `stations` (`id`, `name`, `eatery`) VALUES (%s, %s, %s)"
insert_eatery_hours = "INSERT IGNORE INTO `eatery_hours` (`eatery`, `date`, `daypart`, `start_time`, `end_time`) VALUES (%s, %s, %s, %s, %s)"
insert_menus = "INSERT IGNORE INTO `menus` (`item`, `eatery`, `station`, `date`, `daypart`) VALUES (%s, %s, %s, %s, %s)"


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
        create_eatery_hours = "CREATE TABLE IF NOT EXISTS eatery_hours(date varchar(32), daypart varchar(32), start_time varchar(32), end_time varchar(32), eatery int, foreign key fk_eatery(eatery) references eateries(id) on update cascade on delete restrict)"
        cursor.execute(create_eatery_hours)
        create_menus = "CREATE TABLE IF NOT EXISTS menus(item int, eatery int, station int, date varchar(32), daypart varchar(32), foreign key fk_eatery(eatery) references eateries(id) on update cascade on delete restrict, foreign key fk_item(item) references items(id) on update cascade on delete restrict, foreign key fk_station(station) references stations(id) on update cascade on delete restrict)"
        cursor.execute(create_menus)

    connection.commit()


def process_response(obj):
    with connection.cursor() as cursor:
        items = obj["items"]
        for day in obj["days"]:
            date = day["date"]
            for eatery_id in day["cafes"]:
                # need to access 0th index of this list of lists (unsure why it's a list of lists)
                eatery = day["cafes"][eatery_id]
                dayparts = eatery["dayparts"][0]
                eatery_name = eatery["name"]
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
                            cursor.execute(insert_items, (item_id, item_name, vegetarian, vegan, gluten_free))
                            cursor.execute(insert_eateries, (eatery_id, eatery_name))
                            cursor.execute(insert_stations, (station_id, station_name, eatery_id))
                            cursor.execute(insert_eatery_hours, (eatery_id, date, daypart, starttime, endtime))
                            cursor.execute(insert_menus, (item_id, eatery_id, station_id, date, daypart))
                            connection.commit()


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


def main():
    try:
        create_tables()
        connection.commit()
        for subdir, dirs, files in os.walk("./json"):
            for file in os.listdir(subdir):
                filename = os.fsdecode(file)
                if filename.endswith(".json"):
                    rel_path = str(os.path.join(subdir, filename))
                    with open(rel_path) as datafile:
                        obj = json.load(datafile)
                        process_response(obj)
    finally:
        connection.close()



if __name__ == "__main__":
    main()
