import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
out = open('output/in_book.csv', 'w')
out.write("Name;URL;Author;Price;Number of Ratings;Average Rating" + "\n")
for i in range(0, 5):
	my_url = ("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_"
		+ str(i + 1)
		+ "?ie=UTF8&pg="
		+ str(i + 1))
	uClient = urlopen(my_url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	containers = page_soup.findAll("div", {"class": "zg_itemWrapper"})
	for container in containers:
		URL = "https://www.amazon.in" + container.a["href"]
		try:
			Title = container.find(
				"div", {"class": "p13n-sc-truncate p13n-sc-line-clamp-1"}
				).string.strip()
		except Exception as e:
			Title = container.find(
				"div", {"class": "p13n-sc-truncate p13n-sc-line-clamp-2"}
				).string.strip()
		except AttributeError:
			Title = "Not available"
		try:
			Author = container.find(
				"div", {"class": "a-row a-size-small"}
				).string.strip()
		except AttributeError:
			Author = "Not available"
		try:
			Rating = container.find(
			"span", {"class": "a-icon-alt"}
			).string.strip()
		except AttributeError:
			Rating = "Not available"
		if Rating == "Prime":
			Rating = "Not available"
		try:
			Review = container.find(
				"a", {"class": "a-size-small a-link-normal"}
				).string.strip()
		except AttributeError:
			Review = "Not available"
		try:
			Price = container.find(
			"span", {"class": "p13n-sc-price"}
			).text.strip()
		except AttributeError:
			Price = "Not available"
		out.write(str(Title) + ";")
		out.write(str(URL) + ";")
		out.write(str(Author) + ";")
		out.write(str(Price) + ";")
		out.write(str(Review) + ";")
		out.write(str(Rating) + " \n")
