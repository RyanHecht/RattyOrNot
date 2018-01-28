from datetime import timedelta, date
import requests
import json


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

dining_halls = [ratty, vdub, andrews, blue_room, jos, ivy_room, campus_market, cafe_carts]

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
    date_list = []
    for day in daterange(start_date, end_date):
        date_list.append(str(day))
    print(date_list)
    res = requests.get(base_url + menus, params={"cafe": dining_halls, "date": date_list})
    with open('data.json', 'w') as outfile:
        json.dump(res.json(), outfile)
    process_response(res.json())


def process_response(obj):
    items = obj["items"]
    for day in obj["days"]:
        for cafe in day["cafes"]:
            # need to access 0th index of this list of lists (unsure why it's a list of lists)
            dayparts = cafe["dayparts"][0]
            name = cafe["name"]
            for part in dayparts:
                pass


def main():
    scrape_items(date(2017, 1, 1), date(2018, 1, 1))


if __name__ == "__main__":
    main()
