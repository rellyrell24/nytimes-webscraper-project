from selenium import webdriver
import argparse

parser = argparse.ArgumentParser(description='Web scraper to get news article content.')
parser.add_argument('news_url', metavar='url', type=str,
                    help='The URl where the news NY Times article is located.')
args = parser.parse_args()

chrome_driver_path = "/Users/jerrellgardner/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(args.news_url)

title = driver.find_element_by_xpath('//h1[@data-test-id="headline"]')
print(f"Title: {title.text}")

time = driver.find_elements_by_tag_name("time")
time_text = time[0].text
print(time_text)

content = []
paragraphs_div = driver.find_elements_by_class_name("StoryBodyCompanionColumn")
for div in paragraphs_div:
    paragraphs = div.find_elements_by_tag_name("p")
    for paragraph in paragraphs:
        content.append(paragraph.text)
print("\n".join(content))
driver.close()
