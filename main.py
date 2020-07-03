from bs4 import BeautifulSoup
import requests

search = input("Search for:")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol",{"id" :"b_results"})
links = results.findAll("li",{"class":"b_algo"})
n=1
for item in links:
	print("_____________________________",n,"_____________________________")
	n+=1
	item_text = item.find("a").text
	item_href = item.find("a").attrs["href"]
	
	if item_text and item_href:
		print("Name :",item_text)
		print("Link :",item_href)
		print("Comment :", item.find("a").parent.parent.find("p").text)
		




