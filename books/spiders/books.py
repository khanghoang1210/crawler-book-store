import scrapy

class BookScrapy(scrapy.Spider):
    name = 'books'
    start_urls = ["https://books.toscrape.com/"]
    
    # get all book_urls
    def parse(self, response):
        for next in  response.css("li.col-xs-6 article  div.image_container  a"):
            if next:
                next_link = response.urljoin(next.attrib['href'])
                yield scrapy.Request(next_link, callback=self.parse_new, meta={'start_urls': self.start_urls})

        next_page = response.css("li.next a")
        if next_page:
            next_link_page = response.urljoin(next_page.attrib['href'])
            print("================================")
            print(next_link_page)
            yield scrapy.Request(next_link_page, callback=self.parse)
        else:
            print("================ END STATE ================")

    # get data of each url
    def parse_new(self,respone):
        start_urls = respone.meta['start_urls']
        img_link = respone.css("div.item img::attr(src)").get() 
        poster_link = start_urls[0] + img_link[6:]

        name = respone.css("div.col-sm-6 h1::text").get()
        price = respone.css("div.col-sm-6 p::text").get()
        status = respone.css("div.col-sm-6 p.instock.availability::text").extract()
        if status:
           status = ' '.join(status).strip()

        p_class = respone.css("article  p.star-rating::attr(class)").get()
        stars = p_class.split(' ')[1]

        yield {
            "poster_link": poster_link,
            "book_name": name,
            "book_price": price,
            "status": status,
            "rating": stars 
        }

        # print("=============")
        # print(poster_link)
        # print(name)
        # print(price)
        # print(stars)
        # print(status)

   
            