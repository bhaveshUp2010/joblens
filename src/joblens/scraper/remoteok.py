import requests
from base import JobScraper


class RemoteOKScraper(JobScraper):

    def get_page(self):
        res = requests.get(self.base_url)
        res = res.json()[1:]
        return res

    def get_job(self, raw_data):
        jobs = []
        for job in raw_data:
            jobs.append(job)
        return jobs
