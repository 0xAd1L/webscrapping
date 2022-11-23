from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
soup = BeautifulSoup(webpage.content,"html.parser")

ratings_data = soup.find_all(attrs={"class":"Rating"})

ratings = []
for rating in ratings_data[1:]:
    ratings.append(float(rating.string))
# print(ratings)

plt.hist(ratings)
plt.show()
company_names=[]
company_data=soup.select(".Company")
for company in company_data[1:]:
  company_names.append(company.string)
# print(company_names)

cocoa_data=soup.select(".CocoaPercent")
cocoa_percents=[]
for cocoa in cocoa_data[1:]:
  percent=float(cocoa.get_text().strip("%"))
  cocoa_percents.append(percent)
# print(cocoa_percents)

d = {"Company": company_names, "Ratings": ratings,"CocoaPercentage":cocoa_percents}
my_dataframe=pd.DataFrame.from_dict(d)
print(my_dataframe)
mean_rating=my_dataframe.groupby("Company").Ratings.mean()
# print(mean_rating)
ten_best=mean_rating.nlargest(10)
print(ten_best)


# print(cocoa_percents)
plt.scatter(my_dataframe.CocoaPercentage, my_dataframe.Ratings)

z = np.polyfit(my_dataframe.CocoaPercentage, my_dataframe.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(my_dataframe.CocoaPercentage, line_function(my_dataframe.CocoaPercentage), "r--")

plt.show()
plt.clf()





