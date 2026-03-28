from sqlalchemy import create_engine, Column, String, Float, Text, DateTime
from sqlalchemy.orm import DeclarativeBase, Session
from datetime import datetime

engine = create_engine("sqlite:///C:/study/jobLens/data/raw/joblens.db")


class Base(DeclarativeBase):
    pass


class JobPosting(Base):
    __tablename__ = "postings"
    id = Column(String, primary_key=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    description = Column(Text)
    salary_min = Column(Float)
    salary_max = Column(Float)
    source = Column(String)
    scraped_at = Column(DateTime, default=datetime.utcnow)
    is_remote = Column(String)


Base.metadata.create_all(engine)


def save_posting(postings: list[dict]) -> int:
    saved = 0

    with Session(engine) as session:
        for post in postings:
            if not post.get("id"):
                continue
            record = JobPosting(
                id=post["id"],
                title=post.get("title", ""),
                company=post.get("company", ""),
                location=post.get("location", ""),
                description=post.get("description", ""),
                salary_min=post.get("salary_min"),
                salary_max=post.get("salary_max"),
                source=post.get("source", "unknown"),
                is_remote=post.get("is_remote", "unknown"),
            )

            session.merge(record)
            saved += 1
        session.commit()
    return saved
