from bs4 import BeautifulSoup
import requests

car_companies_url = "https://www.izmostock.com/car-stock-photos-by-brand"
company_links_list = []
for company_link in BeautifulSoup(requests.get(car_companies_url).text, "html.parser").find_all('div', id="by_brand"):
    company_links_list.append(company_link.find("a", href=True)["href"])
print(company_links_list)