#Imports for web scraping and pandas DataFrames
import requests
import pandas as pd
import csv
from sqlalchemy import create_engine, types
import mysql.connector

#Output from a website that converts curl commands to Python from the scraped website
cookies = {
    'zguid': '24|%240315aaad-95c6-414d-bd1e-1de6f3465f41',
    'zgsession': '1|0c2c13d7-1f93-472a-9a61-b3c6c92fb6aa',
    'zjs_anonymous_id': '%220315aaad-95c6-414d-bd1e-1de6f3465f41%22',
    'zjs_user_id': 'null',
    'zg_anonymous_id': '%22271b59a0-608d-4fa4-8ad5-f648f5ccf718%22',
    '_ga': 'GA1.2.1343471.1709652208',
    '_gid': 'GA1.2.1920060055.1709652208',
    'pxcts': '51e91029-db04-11ee-bbb7-628094349d4e',
    '_pxvid': '51e8fee4-db04-11ee-bbb7-c6d91f170a41',
    '_gcl_au': '1.1.825464755.1709652212',
    'DoubleClickSession': 'true',
    '_pin_unauth': 'dWlkPVpXVXpOek13TUdZdFpUazJNUzAwWkRreUxUaGxOV1F0WW1GbE1qVTNaVGc1WWpGbA',
    '__pdst': 'b238344703374409892a97855954d2ab',
    '_fbp': 'fb.1.1709652213088.232235615',
    '_clck': 'kkds9a%7C2%7Cfjt%7C0%7C1525',
    'JSESSIONID': '22C65951671D11379F451040FF8FD4F7',
    'tfpsi': 'cba97832-3e1f-4712-80ba-92cfa8c34501',
    'x-amz-continuous-deployment-state': 'AYABeHs7dikmTv5KZCDtnTSMFP0APgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADFU4f9xK+wkFVgJPWQAwIODZI63PnX1ZEy5ty5ZJKzjOUtCpBTa%2FCPUtrCn2X6SI49%2FOGUnPVVc65Sx5ib57AgAAAAAMAAQAAAAAAAAAAAAAAAAAADlsQiwzZjtYONI2reBYFGb%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAwS1v3AjrxwXoJZ2+LMe0berI2CQjnACrbSXokU2CQjnACrbSXokQ==',
    '_gac_UA-21174015-56': '1.1709658528.CjwKCAiAopuvBhBCEiwAm8jaMUiYCwCrEd4-Yzj2agBgR1HXx9RTJ0HloCRQjLoVhqjHveBYdUEZFRoCGVMQAvD_BwE',
    'zjs_utmsource': '%22google%22',
    'zjs_utmmedium': '%22cpc%22',
    'zjs_utmcontent': '%221471764169|65545421228|kwd-570802407|603457706088|%22',
    '_gcl_aw': 'GCL.1709658534.CjwKCAiAopuvBhBCEiwAm8jaMUiYCwCrEd4-Yzj2agBgR1HXx9RTJ0HloCRQjLoVhqjHveBYdUEZFRoCGVMQAvD_BwE',
    '_hp2_ses_props.1215457233': '%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22us%22%3A%22google%22%2C%22um%22%3A%22cpc%22%2C%22uc%22%3A%221471764169%7C65545421228%7Ckwd-570802407%7C603457706088%7C%22%2C%22ts%22%3A1709658536761%2C%22d%22%3A%22www.zillow.com%22%2C%22h%22%3A%22%2F%22%7D',
    '_hp2_id.1215457233': '%7B%22userId%22%3A%225423646040404048%22%2C%22pageviewId%22%3A%226663611743090612%22%2C%22sessionId%22%3A%228542769867492817%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
    'AWSALB': '/FYP+Jzjp5f2Aa/UrEAtauU0uKmEKkQ/dJqcleDFLYUWIOvBGFcZz4KJobbQYUYvcp3GKzprBMczgC0EodL5cSp3F7Ld8b+DHfZOSR4K1lIi2OS40hfio2sVxu81',
    'AWSALBCORS': '/FYP+Jzjp5f2Aa/UrEAtauU0uKmEKkQ/dJqcleDFLYUWIOvBGFcZz4KJobbQYUYvcp3GKzprBMczgC0EodL5cSp3F7Ld8b+DHfZOSR4K1lIi2OS40hfio2sVxu81',
    '_px3': 'b0062e9e74fafee0adc54f1eb2cc1efe8306297eaa884f25f21f550d5e95fd61:8fdde7Z7IyXoYZOhIju+N6dlnBCQZD/safPuwTW7xBGRUKwAE7tuNo/Xq/dxz6xd7Xmjw/rgZHduz+sk67twuw==:1000:roGSjucK2uxpqgALD/PokZ/Idxf6lhwqwYIDHSoDl0X2ux5Pau7ohPV98yCHfGQ7FLsLqMy6orSg609m1AO1KCpdgDMmU9FYFB6HjVkfWF1nQ/tkCIoAReBXg2QdzsZiXk2NTj0bxyf3x47COyZupuft6xd+JJtB/F7wcMeS/wTatCOUcIKbMjsxosnJeiIc7k9J7BrADeaCw+HYXDD4LE3yXedA2DUyp6RXzh1pR5Y=',
    '__gads': 'ID=ab6ab78f906b6bb6:T=1709652222:RT=1709658890:S=ALNI_Mb6rXnjHijhQBbZt2GM8ZtszFS0rQ',
    '__gpi': 'UID=00000dcf74664daf:T=1709652222:RT=1709658890:S=ALNI_MYKR6I6-lDb5bmRBTp7rvJlMLQyTg',
    '__eoi': 'ID=78a45794c5d02e2e:T=1709652222:RT=1709658890:S=AA-Afjbr6n0Qql_XH2Lcg3StOTvC',
    '_uetsid': '53b9b1f0db0411eebf5591c92eeb9d3d',
    '_uetvid': '53b9ab20db0411eeb84d73342c1e20e6',
    '_gat': '1',
    'search': '6|1712250980511%7Crect%3D36.98331%2C-84.568922%2C36.602408%2C-85.058534%26rid%3D76402%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26student-housing%3D0%26income-restricted-housing%3D0%26military-housing%3D0%26disabled-housing%3D0%26senior-housing%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0976402%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09',
    '_clsk': 'rv2snv%7C1709658998319%7C14%7C0%7Cs.clarity.ms%2Fcollect',
}

headers = {
    'authority': 'www.zillow.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'zguid=24|%240315aaad-95c6-414d-bd1e-1de6f3465f41; zgsession=1|0c2c13d7-1f93-472a-9a61-b3c6c92fb6aa; zjs_anonymous_id=%220315aaad-95c6-414d-bd1e-1de6f3465f41%22; zjs_user_id=null; zg_anonymous_id=%22271b59a0-608d-4fa4-8ad5-f648f5ccf718%22; _ga=GA1.2.1343471.1709652208; _gid=GA1.2.1920060055.1709652208; pxcts=51e91029-db04-11ee-bbb7-628094349d4e; _pxvid=51e8fee4-db04-11ee-bbb7-c6d91f170a41; _gcl_au=1.1.825464755.1709652212; DoubleClickSession=true; _pin_unauth=dWlkPVpXVXpOek13TUdZdFpUazJNUzAwWkRreUxUaGxOV1F0WW1GbE1qVTNaVGc1WWpGbA; __pdst=b238344703374409892a97855954d2ab; _fbp=fb.1.1709652213088.232235615; _clck=kkds9a%7C2%7Cfjt%7C0%7C1525; JSESSIONID=22C65951671D11379F451040FF8FD4F7; tfpsi=cba97832-3e1f-4712-80ba-92cfa8c34501; x-amz-continuous-deployment-state=AYABeHs7dikmTv5KZCDtnTSMFP0APgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADFU4f9xK+wkFVgJPWQAwIODZI63PnX1ZEy5ty5ZJKzjOUtCpBTa%2FCPUtrCn2X6SI49%2FOGUnPVVc65Sx5ib57AgAAAAAMAAQAAAAAAAAAAAAAAAAAADlsQiwzZjtYONI2reBYFGb%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAwS1v3AjrxwXoJZ2+LMe0berI2CQjnACrbSXokU2CQjnACrbSXokQ==; _gac_UA-21174015-56=1.1709658528.CjwKCAiAopuvBhBCEiwAm8jaMUiYCwCrEd4-Yzj2agBgR1HXx9RTJ0HloCRQjLoVhqjHveBYdUEZFRoCGVMQAvD_BwE; zjs_utmsource=%22google%22; zjs_utmmedium=%22cpc%22; zjs_utmcontent=%221471764169|65545421228|kwd-570802407|603457706088|%22; _gcl_aw=GCL.1709658534.CjwKCAiAopuvBhBCEiwAm8jaMUiYCwCrEd4-Yzj2agBgR1HXx9RTJ0HloCRQjLoVhqjHveBYdUEZFRoCGVMQAvD_BwE; _hp2_ses_props.1215457233=%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22us%22%3A%22google%22%2C%22um%22%3A%22cpc%22%2C%22uc%22%3A%221471764169%7C65545421228%7Ckwd-570802407%7C603457706088%7C%22%2C%22ts%22%3A1709658536761%2C%22d%22%3A%22www.zillow.com%22%2C%22h%22%3A%22%2F%22%7D; _hp2_id.1215457233=%7B%22userId%22%3A%225423646040404048%22%2C%22pageviewId%22%3A%226663611743090612%22%2C%22sessionId%22%3A%228542769867492817%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; AWSALB=/FYP+Jzjp5f2Aa/UrEAtauU0uKmEKkQ/dJqcleDFLYUWIOvBGFcZz4KJobbQYUYvcp3GKzprBMczgC0EodL5cSp3F7Ld8b+DHfZOSR4K1lIi2OS40hfio2sVxu81; AWSALBCORS=/FYP+Jzjp5f2Aa/UrEAtauU0uKmEKkQ/dJqcleDFLYUWIOvBGFcZz4KJobbQYUYvcp3GKzprBMczgC0EodL5cSp3F7Ld8b+DHfZOSR4K1lIi2OS40hfio2sVxu81; _px3=b0062e9e74fafee0adc54f1eb2cc1efe8306297eaa884f25f21f550d5e95fd61:8fdde7Z7IyXoYZOhIju+N6dlnBCQZD/safPuwTW7xBGRUKwAE7tuNo/Xq/dxz6xd7Xmjw/rgZHduz+sk67twuw==:1000:roGSjucK2uxpqgALD/PokZ/Idxf6lhwqwYIDHSoDl0X2ux5Pau7ohPV98yCHfGQ7FLsLqMy6orSg609m1AO1KCpdgDMmU9FYFB6HjVkfWF1nQ/tkCIoAReBXg2QdzsZiXk2NTj0bxyf3x47COyZupuft6xd+JJtB/F7wcMeS/wTatCOUcIKbMjsxosnJeiIc7k9J7BrADeaCw+HYXDD4LE3yXedA2DUyp6RXzh1pR5Y=; __gads=ID=ab6ab78f906b6bb6:T=1709652222:RT=1709658890:S=ALNI_Mb6rXnjHijhQBbZt2GM8ZtszFS0rQ; __gpi=UID=00000dcf74664daf:T=1709652222:RT=1709658890:S=ALNI_MYKR6I6-lDb5bmRBTp7rvJlMLQyTg; __eoi=ID=78a45794c5d02e2e:T=1709652222:RT=1709658890:S=AA-Afjbr6n0Qql_XH2Lcg3StOTvC; _uetsid=53b9b1f0db0411eebf5591c92eeb9d3d; _uetvid=53b9ab20db0411eeb84d73342c1e20e6; _gat=1; search=6|1712250980511%7Crect%3D36.98331%2C-84.568922%2C36.602408%2C-85.058534%26rid%3D76402%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26student-housing%3D0%26income-restricted-housing%3D0%26military-housing%3D0%26disabled-housing%3D0%26senior-housing%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0976402%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09; _clsk=rv2snv%7C1709658998319%7C14%7C0%7Cs.clarity.ms%2Fcollect',
    'origin': 'https://www.zillow.com',
    'referer': 'https://www.zillow.com/monticello-ky-42633/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Afalse%2C%22mapBounds%22%3A%7B%22west%22%3A-85.058534%2C%22east%22%3A-84.568922%2C%22south%22%3A36.602408%2C%22north%22%3A36.98331%7D%2C%22usersSearchTerm%22%3A%2242633%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A76402%2C%22regionType%22%3A7%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

json_data = {
    'searchQueryState': {
        'pagination': {},
        'isMapVisible': False,
        'mapBounds': {
            'west': -85.058534,
            'east': -84.568922,
            'south': 36.602408,
            'north': 36.98331,
        },
        'usersSearchTerm': '42633',
        'regionSelection': [
            {
                'regionId': 76402,
                'regionType': 7,
            },
        ],
        'filterState': {
            'sortSelection': {
                'value': 'globalrelevanceex',
            },
            'isAllHomes': {
                'value': True,
            },
            'isTownhouse': {
                'value': False,
            },
            'isMultiFamily': {
                'value': False,
            },
            'isCondo': {
                'value': False,
            },
            'isLotLand': {
                'value': False,
            },
            'isApartment': {
                'value': False,
            },
            'isManufactured': {
                'value': False,
            },
            'isApartmentOrCondo': {
                'value': False,
            },
        },
        'isListVisible': True,
    },
    'wants': {
        'cat1': [
            'listResults',
        ],
        'cat2': [
            'total',
        ],
    },
    'requestId': 8,
    'isDebugRequest': False,
}

response = requests.put('https://www.zillow.com/async-create-search-page-state', cookies=cookies, headers=headers, json=json_data)

results_json = response.json()

result_items = results_json['cat1']['searchResults']['listResults']

#Arrays for the relevant columns to be made
address = []
price = []
beds = []
baths = []
area = []
url = []
propertyType = []
measurement = []

#For loop to fill each array
for result in result_items:
 address.append(result['addressStreet'])
 price.append(result['unformattedPrice'])
 baths.append(result['baths'])
 beds.append(result['beds'])
 area.append(result['area'])
 url.append(result['detailUrl'])
 propertyType.append(result['hdpData']['homeInfo']['homeType'])
 #Column to specify unit of measurment
 measurement.append("sqft")

#Creating a DataFrame 
zillow_df = pd.DataFrame({'Address':address, 'Price':price, 'Beds':beds, 'Baths':baths, 'Area':area, 'Measurement':measurement, 'Property Type':propertyType,'URL':url})

#Saving the DataFrame to a .csv
zillow_df.to_csv('zillow_homes.csv', index=False)

#connecting to SQL
host = 'localhost'
user = 'root'
password = ''
database = 'properties'

#creating .csv file
csv_file_path = 'zillow_homes.csv'

#creating/updating the zillow_homes table
table_name = 'zillow_homes'

df = pd.read_csv(csv_file_path)

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

df.to_sql(name=table_name, con=engine,if_exists='replace', index=False)

engine.dispose()

#output upon successful table creation/update
print("zillow_homes has been made/replaced")