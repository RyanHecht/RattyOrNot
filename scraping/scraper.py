from datetime import timedelta, date
import requests

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

response = requests.get(base_url + cafes, params={"cafe": 1531})
print(response.content)

def daterange(start_date, end_date):
    """
    produces dates in a range! taken from
    https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
    """
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def scrape_items(start_date, end_date):
    for hall in dining_halls:
        pass


if __name__ == "__main__":
    pass
