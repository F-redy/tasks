import scrapy


class BooksCrawlSpider(scrapy.Spider):
    name = "books_crawl"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response, **kwargs):
        books = response.xpath("//ol[@class='row']/li")
        for book in books:
            yield {
                # .// - что бы не парсилась одна и та же книга
                'image': book.xpath(".//div[@class='image_container']/a/img/@src").get(),
                'title': book.xpath(".//h3/a/@title").get(),
                'price': book.xpath(".//p[@class='price_color']/text()").get(),
            }

# start scraping: scrapy crawl books_crawl
# save to file:
# scrapy crawl books_crawl -o books.json
# scrapy crawl books_crawl -o books.csv