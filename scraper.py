from requests_html import AsyncHTMLSession
asession = AsyncHTMLSession()

async def get_articles():
    r = await asession.get('https://www.finn.no/realestate/homes/search.html?location=0.20012&property_type=3&sort=PUBLISHED_DESC')
    res = []
    articles = r.html.find('article')
    for article in articles:
        res.append(article.text)
    return res

articles_text = asession.run(get_articles)

with open("leiligheter_i_rogaland.txt", "w") as file:
    file.write("\n\n".join(articles_text[0]))