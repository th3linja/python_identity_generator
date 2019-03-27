from bs4 import BeautifulSoup
import requests


def strip_value(str):
    if ('value="') in str:
        text_beg = str.index('value="') + 7
        text_end = str.index('"/></div>')
        str = str[text_beg:text_end]
        return str
    if ('<p>') in str:
        text_beg = str.index('<p>') + 3
        text_end = str.index('</p>')
        str = str[text_beg:text_end]
        return str
    return str


person_data = {}

url = 'https://www.fakepersongenerator.com/Index/generate'
req = requests.post(url)
page = requests.get(req.url)

soup = BeautifulSoup(page.content, 'html.parser')
category = soup.select('.info-title')

name_raw = soup.select('.click')
data_raw = str(soup.select('.col-md-8'))
data2 = soup.select('.info-detail')

index = data_raw.find('<p')                             # index for parsing data_raw

name = name_raw[0].string.strip()
data_main = []
data_main_val = []

while index != -1:
    iterator = 1
    index2 = data_raw.find('<p', index + iterator)
    build_string = data_raw[index + 3: index2 - 4]
    data_main.append(build_string)
    index = index2
    iterator += 1

for a in range(len(data_main)):
    data_main[a] = data_main[a].replace('<b>', '')
    data_main[a] = data_main[a].replace('</b>', '')
    data_main[a] = data_main[a].replace('title="test">', '')
    data_main_val.append(data_main[a][data_main[a].index(':') + 2 :])
    data_main[a] = data_main[a][:data_main[a].index(':')]
    person_data[data_main[a]] = data_main_val[a]


for b in range(len(data2)):
    category[b] = category[b].string.strip()
    data2[b] = strip_value(str(data2[b]))
    data2[b] = data2[b].replace('&lt;', '<')
    data2[b] = data2[b].replace('<br/>', '\n\t\t')
    data2[b] = data2[b].replace('&quot;', '"')
    person_data[category[b]] = data2[b]


class Person(object):
    def __init__(self):
        self.name = name
        self.gender = person_data.get('Gender)')
        self.race = person_data.get('Race')
        self.birthday = person_data.get('Birthday')
        self.street = person_data.get('Street')
        self.city_state_zip = person_data.get('City, State, Zip')
        self.telephone = person_data.get('Telephone')
        self.mobile = person_data.get('Mobile')
        self.email = person_data.get("Email")
        self.height = person_data.get("Height")
        self.weight = person_data.get("Weight")
        self.hair_color = person_data.get("Hair Color")
        self.blood_type = person_data.get("Blood Type")
        self.zodiac = person_data.get('Starsign(Tropical Zodiac)')
        self.mother_maiden_name = person_data.get("Mother's Maiden Name")
        self.civil_status = person_data.get("Civil Status")
        self.educational_background = person_data.get("Educational Background")
        self.disease_history = person_data.get("Disease History")
        self.social_security = person_data.get("Social Security Number")
        self.passport = person_data.get("Passport")
        self.driver_license = person_data.get("Driver License")
        self.car_license_plate = person_data.get("Car License Plate")
        self.employment_status = person_data.get("Employment Status")
        self.monthly_salary = person_data.get("Monthly Salary")
        self.occupation = person_data.get("Occupation(Job Title)")
        self.company_name = person_data.get("Company Name")
        self.company_size = person_data.get("company_Size")
        self.industry = person_data.get("Industry")
        self.credit_card_type = person_data.get("Credit Card Type")
        self.credit_card_number = person_data.get("Credit Card Number")
        self.cvv2 = person_data.get("CVV2")
        self.expires = person_data.get("Expires")
        self.paypal = person_data.get("Paypal")
        self.western_union_mtcn = person_data.get("Western Union MTCN")
        self.moneygram_mtcn = person_data.get("MoneyGram MTCN")
        self.account_balance = person_data.get("Account Balance")
        self.orders_lifetime = person_data.get("Orders Lifetime")
        self.total_consumption = person_data.get("Total Consumption")
        self.preferred_payment = person_data.get("Preferred Payment")
        self.family_members = person_data.get("Family Members")
        self.vehicle = person_data.get("Vehicle")
        self.online_status = person_data.get("Online Status")
        self.online_signature = person_data.get("Online Signature")
        self.online_biography = person_data.get("Online Biography")
        self.interest = person_data.get("Interest")
        self.favorite_color = person_data.get("Favorite Color")
        self.favorite_movie = person_data.get("Favorite Movie")
        self.favorite_music = person_data.get("Favorite Music")
        self.favorite_song = person_data.get("Favorite Song")
        self.favorite_book = person_data.get("Favorite Book")
        self.favorite_sports = person_data.get("Favorite Sports")
        self.favorite_tv = person_data.get("Favorite TV")
        self.favorite_movie_star = person_data.get("Favorite Movie Star")
        self.favorite_singer = person_data.get("Favorite Singer")
        self.favorite_food = person_data.get("Favorite Food")
        self.personality = person_data.get("Personality")
        self.person_style = person_data.get("Personal Style")
        self.website = person_data.get("Website")
        self.register_time = person_data.get("Register Time")
        self.register_ip = person_data.get("Register IP")
        self.last_login_time = person_data.get("Last Login Time")
        self.last_login_ip = person_data.get("Last Login IP")
        self.login_times = person_data.get("Login Times")
        self.online_time = person_data.get("On-line Time")
        self.points = person_data.get("Points")
        self.level = person_data.get("Level")
        self.number_of_comments = person_data.get("Number of Comments")
        self.posted_articles = person_data.get("Posted Articles")
        self.friends = person_data.get("Friends")
        self.online_now = person_data.get("Online Now")
        self.member_center_viewed = person_data.get("Member Center Viewed")
        self.language = person_data.get("Language")
        self.referer_id = person_data.get("Referer ID")
        self.subscribed_or_not = person_data.get("Subscribed or Not")
        self.allow_notice = person_data.get("Allow Notice")
        self.verified_status = person_data.get("Verified Status")
        self.security_question = person_data.get("Security Question")
        self.security_answer = person_data.get("Security Answer")
        self.browser_user_agent = person_data.get("Browser User Agent")
        self.system = person_data.get("System")
        self.guid = person_data.get("GUID")
        self.geo_coordinates = person_data.get("Geo coordinates")
        self.timezone = person_data.get("Timezone")
        self.ups_tracking = person_data.get("UPS Tracking Number")
        self.country = person_data.get("Country")
        self.country_code = person_data.get("Country Code")

person = Person()
print(person.name)
