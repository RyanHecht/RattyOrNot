from datetime import timedelta, date
import os
import requests
import json
import time

base_url = "http://legacy.cafebonappetit.com/api/2/"
cafes = "cafes"
menus = "menus"
items = "items"
ratty = 1531
vdub = 1532
andrews = 1533
blue_room = 1534
jos = 1535
ivy_room = 1536
campus_market = 1537
cafe_carts = 1538

eatery_map = {}
eatery_map[ratty] = "ratty"
eatery_map[vdub] = "vdub"
eatery_map[andrews] = "andrews"
eatery_map[blue_room] = "blue_room"
eatery_map[jos] = "jos"
eatery_map[ivy_room] = "ivy_room"
eatery_map[campus_market] = "campus_market"

dining_halls = [ratty, vdub, andrews, blue_room, jos, ivy_room, campus_market]

# response = requests.get(base_url + menus, params={"cafe": 1531, "date": ["2017-01-01", "2017-01-27"]})
# print(response.json()["days"])
# with open('data.json', 'w') as outfile:
#     json.dump(response.json(), outfile)

def daterange(start_date, end_date):
    """
    produces dates in a range! taken from
    https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
    """
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def scrape_items(start_date, end_date):
    """
    Scrapes all dining halls from start_date to end_date for all their items
    and inserts them into the db.
    """
    filename = str(start_date) + ":" + str(end_date) + ".json"
    for day in daterange(start_date, end_date):
        for hall in dining_halls:
            res = requests.get(base_url + menus, params={"cafe": hall, "date": str(day)})
            time.sleep(1)
            if not res:
                print("res was none", str(day), res.status_code)
                time.sleep(4)
                continue
            filename = "json/" + str(eatery_map[hall]) + "/" + str(day) + ".json"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, 'w') as outfile:
                json.dump(res.json(), outfile)


def main():
    scrape_items(date(2017, 9, 16), date(2017, 9, 30))


if __name__ == "__main__":
    main()
