import requests
from base import JobScraper


class RemoteOkScraper(JobScraper):

    def get_page(self):
        header = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(self.base_url, headers=header)

        return res.json()[1:]

    def get_job(self, raw_data):
        postings = []

        for job in raw_data:
            post = {
                "id": job["id"],
                "title": job.get("position", ""),
                "company": job.get("company", ""),
                "location": job.get("location") or "Remote",
                "description": job.get("description", ""),
                "source": "remoteok",
                "salary_min": job.get("salary_min"),
                "salary_max": job.get("salary_max"),
                "is_remote": "yes",
            }
            postings.append(post)

        return postings
