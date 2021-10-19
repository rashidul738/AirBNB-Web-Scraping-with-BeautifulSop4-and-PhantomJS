from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

class Details(object):
	def __init__(self):
		self.link = ""

def get_airbnb_details():
	driver = webdriver.PhantomJS(executable_path = r'G:\Projects\20 real webscraping projects\phantomjs.exe')
	URL = 'https://www.airbnb.com/s/NYC--NY--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=june&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2021-05-20&checkout=2021-06-09&source=structured_search_input_header&search_type=filter_change&place_id=ChIJOwg_06VPwokRYv534QaPC8g&adults=1'

	driver.get(URL)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	div = soup.find('div', {'class': "_fhph4u"})
	link_list = []
	for data in div.findAll('div', {"itemprop": "itemListElement"}):
		link = f"https://www.airbnb.com{data.a['href']}"
		# print(link)
		new_link = Details()
		new_link.link = link
		link_list.append(new_link)
	driver.quit()
	return link_list


def get_airbnb_all_details(link_list):
	driver = webdriver.Chrome(executable_path = r'G:\Projects\20 real webscraping projects\chromedriver.exe')
	driver.maximize_window()
	for row in link_list:
		driver.get(row.link)
		sleep(5)

		soup1 = BeautifulSoup(driver.page_source, 'lxml')
		
		div = soup1.find('div', class_ = '_mbmcsn')
		name = div.h1.text

		span = soup1.find('span', {'class': "_169len4r"})

		city = span.text.split(',')[0]

		state = span.text.split(',')[1]
		try:
			country = span.text.split(',')[2]
		return country	
		except:
			print('City not available')	
		guest = soup1.find('div', {'class': "_tqmy57"})
		span2 = guest.findAll('span')
		guests = span2[0].text

		bedroom = span2[2].text
		bed = span2[4].text
		try:
			baths = span2[6].text
		except:
			print("Baths is not available")	

		span3 = soup1.find('div', class_ = "_1l4zat7")
		price = span3.span.text

		info = {
		'name': name,
		'city': city,
		'state': state,
		'Country': country,
		'guests': guests,
		'bedroom': bedroom,
		'bed': bed,
		'baths': baths,
		'price': price,
		'Link': row.link
		}
		print(info)	

	driver.quit()
	return link_list

get_airbnb_all_details(get_airbnb_details())

	


