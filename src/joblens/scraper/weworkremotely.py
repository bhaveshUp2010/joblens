import requests
from bs4 import BeautifulSoup
from base import JobScraper


class WWRScraper(JobScraper):

    def get_page(self):
        header = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(self.base_url, headers=header)
        return res.text

    def get_job(self, raw_data):
        soup = BeautifulSoup(raw_data, "xml")
        posting = []
        all_jobs = soup.find_all("item")
        for job in all_jobs:
            post = {
                "title": job.title.text if job.title else "N/A",
                "link": job.link.text if job.link else "N/A",
                "category": job.category.text if job.category else "N/A",
                "region": job.region.text if job.region else "N/A",
                "description": job.description.text if job.description else "N/A",
            }
            posting.append(post)
        return posting
