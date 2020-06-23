import scrapy

class VonObenSpider(scrapy.Spider):
    name = 'vonobenspider'
    start_urls = ['https://www.wien.gv.at/spezial/vonoben/innere-stadt']

    def parse(self, response):
        for article in response.css('article.js-slide'):
            title_field = article.css('.slide-info__heading')
            title = title_field.css('::text').get().strip()
            info_text_field = article.css('.js-slide-info-text')
            try:
                info_text = info_text_field.css('::text').get().strip()
            except:
                info_text = ""
            image_field = article.css("a.slide-info__download")
            image = image_field.css('::attr("href")').get().split('/')[-1]

            yield {'title': title,
                   'info_text': info_text,
                   'image': image}

        next_button = response.css('button.slide-btn--next')
        if next_button:
            next_url = next_button.css('::attr("data-next")').get()
            if next_url != '/spezial/vonoben/':  # this is the url on the last page
                yield response.follow(next_url, self.parse)
