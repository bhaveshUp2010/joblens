from remoteok import RemoteOKScraper

remote = RemoteOKScraper("https://remoteok.com/api")

remote_job_listings = remote.scrape()

print(remote_job_listings[0])
print(len(remote_job_listings))
print(type(remote_job_listings))
