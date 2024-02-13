def read_file():
    with open('web_scraping/all_urls.txt', 'r') as f:
        read_list = [line.rstrip('\n') for line in f]
    return read_list
