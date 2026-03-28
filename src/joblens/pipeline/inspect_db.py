from sqlalchemy.orm import Session
from storage import engine, JobPosting


def inspect_DB():
    with Session(engine) as session:
        total = session.query(JobPosting).count()
        sample = session.query(JobPosting).limit(5).all()

        print(f"Total postings in DB: {total}")
        for p in sample:
            print(f"  [{p.source}] {p.title} @ {p.company} | salary: {p.salary_max}")


if __name__ == "__main__":
    inspect_DB()
