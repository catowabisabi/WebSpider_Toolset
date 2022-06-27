def ingest_wiki():
    # ticker example
    ticker_list = ['AAPL.O', 'LVS', 'JPM', 'XOM', '005930.KS']
    ticker_name = ['APPLE INC', 'LAS VEGAS SANDS CORP', 'JPMORGAN CHASE & CO', 'EXXON MOBIL CORP', 'SAMSUNG ELECTRONICS']

    news = []
    links = []
    tickers = []
    df = pd.DataFrame()

    for t in ticker_name:
        # get company description from ingest_wikipedia function
        doc = ingest_wikipedia(t)
        news.append(doc[0])
        links.append(doc[1])
    
    # store to csv
    df['ticker'] = ticker_list
    df['ticker_name'] = ticker_name
    df['link'] = links
    df['news'] = news
    df.to_csv('data_news/wikipedia-tickers.csv')

    del news, links, tickers
    
# FUNCTION FOR WIKIPEDIA INGESTION
def ingest_wikipedia(ticker_name):
    # set header
    headers = random_header()

    # query for wikipedia and tickername
    url = f"https://www.google.com/search?q=wikipedia {ticker_name.lower()} company&lr=lang_en&hl=en"
    res = requests.get(url, headers=headers)
    # status = res.raise_for_status()

    url_w = []
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    links = soup.select(".yuRUbf a")
    
    for link in links[:5]:
        url_w.append(link.get("href"))
    
    print(url_w[0])

    # open wikipedia site and get company description
    try:
        scrapped_data = urllib.request.urlopen(url_w[0])

        article = scrapped_data.read()
        parsed_article = bs4.BeautifulSoup(article,'lxml')
        paragraphs = parsed_article.find_all('p')
        article_text = ""

        for p in paragraphs:
            article_text += p.text
            
        link = url_w[0]

    except Exception as e:
        article_text = ''
        link = ''

    # return company description and wikipedia link
    return article_text, link