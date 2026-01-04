"""
Scraping site auto.ria.com
Author: Cod3W1ld01@proton.me
"""
import os
import scrapy


class AppAutoriaSpider(scrapy.Spider):
    """
    Scraping site auto.ria.com
    """
    name = "app_autoria"
    allowed_domains = ["auto.ria.com"]

    def __init__(self, *args, url: str = os.getenv("URL_TARGET"),
                 end_page: int = 2, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.end_page = end_page
        n: int = int(os.getenv("COUNT_PAGES"))
        print(n)
        print(url)
        self.start_urls = [
            f"{self.url}&page={i}" for i in range(1, n)
        ]

    def parse(self, response):
        """
        Scraping site auto.ria.com
        :param response:
        :return:
        """
        contents = response.css("div.gap-32.items-list>a")
        for content in contents:
            title = (content.css(
                "div.common-text.size-16-20.titleS.fw-bold.mb-4::text")
                     .get())
            if not title:
                continue

            description = (content.css(
                "div.common-text.size-14-16.ellipsis-1.mb-8::text")
                           .get())
            price_usd = (content.css(
                "span.common-text.titleM.c-green::text")
                         .get())
            if price_usd:
                price_usd = int(price_usd.replace("\xa0", "")
                                .replace("$", "")
                                .strip())

            price_hrn = content.css("span.common-text.body::text").get()
            if price_hrn:
                price_hrn = (price_hrn.replace("\xa0", "")
                             .replace("·", "")
                             .replace("грн", "").strip())

            blocks = content.css("span.common-text.ellipsis-1.body::text")
            distance = blocks[0].get() if len(blocks) > 0 else None
            switch_resource = blocks[1].get() if len(blocks) > 1 else None
            type_fuel = blocks[2].get() if len(blocks) > 2 else None
            city = blocks[3].get() if len(blocks) > 3 else None

            context = content.css("span::text").getall()
            description_full = (content.css(
                "p.common-text.footnote.mt-12.ellipsis-1::text")
                                .get())

            yield {
                "title": title,
                "short_description": description,
                "price_usd": price_usd,
                "price_hrn": price_hrn,
                "city": city,
                "distance": distance,
                "switch_resource": switch_resource,
                "type_fuel": type_fuel,
                "context": context,
                "description": description_full,
            }
