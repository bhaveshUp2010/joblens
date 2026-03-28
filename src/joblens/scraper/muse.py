import requests
from bs4 import BeautifulSoup
from base import JobScraper


class MuseScraper(JobScraper):

    def get_page(self):
        header = {"User-Agent": "Mozilla/5.0"}
        param = {"page": 1}
        res = requests.get(self.base_url, headers=header, params=param)

        return res.json()

    def get_job(self, raw_data):

        jobs = raw_data.get("results", [])
        posting = []
        for job in jobs:
            html = job.get("contents")
            soup = BeautifulSoup(html, "html.parser")
            post = {
                "title": job.get("name"),
                "company": job.get("company").get("name"),
                "location": job.get("locations"),
                "description": soup.get_text(separator=" "),
            }
            posting.append(post)

        return posting
