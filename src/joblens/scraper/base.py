from abc import ABC, abstractmethod


class JobScraper(ABC):

    def __init__(self, base_url):
        self.base_url = base_url

    @abstractmethod
    def get_page(self):
        pass

    @abstractmethod
    def get_job(self, raw_data):
        pass

    def scrape(self):
        raw_data = self.get_page()
        job_data = self.get_job(raw_data)
        return job_data
