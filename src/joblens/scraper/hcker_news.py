import requests
from bs4 import BeautifulSoup
from base import JobScraper


class HNWHScraper(JobScraper):

    def get_page(self):
        url = self.base_url
        header = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=header)
        return res.text

    def get_job(self, raw_data):

        soup = BeautifulSoup(raw_data, "html.parser")
        comments = soup.find_all("tr", {"class": "athing comtr"})

        jobs = []
        for c in comments:
            user_tag = c.find("a", class_="hnuser")
            user = user_tag.text if user_tag else ""

            text_tag = c.find("div", {"class": "commtext"})
            if not text_tag:
                continue

            raw_text = text_tag.get_text("\n", strip=True)
            jobs.append({"user": user, "text": raw_text})

        return jobs
