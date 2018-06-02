import scrapy

# this class should be in spider folder
# scrapy will find its spiders here
# creates a class for a spider
# inherits spider class
# this spider class is much like a interface to use the scrapy content
class QuotesWebScraoer(scrapy.Spider):

    # Name to refer to the spider
    name = "quotes_spider"

    def start_requests(self):
        # list of urls to scrape
        # First extract content from first page then next page
        # Entire html will be extrxted in this example
        start_urls = [
            "http://quotes.toscrape.com/page/1/",
            "http://quotes.toscrape.com/page/2/"
        ]

        # loop thorugh urls
        # pass requests
        for url in  start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, responses):
        # extract the page number
        page = responses.url.split("/")[-2]

        # name of the file which save the content to
        # parse the string to %S
        filename = "scrapy_tutorial/dump/quotes.%s.html" % page

        # store the html content
        with open(filename, "wb") as file:
            file.write(responses.body)
        self.log("Saved file %s " % filename)