import scrapy
from scrapy.http import FormRequest
import requests 
from http import cookies

#scrapy crawl linkedin_people_profile
class LinkedInPeopleProfileSpider(scrapy.Spider):
    name = "linkedin_test"

    custom_settings = {
        'FEEDS': { 'data/%(name)s_%(time)s.jsonl': { 'format': 'jsonlines',}}
        }

    def start_requests(self):
        login_url = 'https://www.linkedin.com/uas/login'
        yield scrapy.Request(login_url, callback=self.login)


    def login(self, response):
        token = response.css('form input[name="csrf_token"]::attr(value)').extract_first()
        return FormRequest.from_response(response,
            formdata={'session_key': '@gmail.com', 'session_password': '!'},
            callback=self.after_login)

    def after_login(self, response):
        profile_list = ['semirsakanovic']