import sys
from sqlalchemy import create_engine, Column, Integer, Date, Time, desc
from sqlalchemy.orm import declarative_base
import os

# engine = create_engine('sqlite:////var/log/gilfoyle/database.db')
dbPath = "database.db"
if os.path.realpath(__file__) == "/usr/local/bin/gilfoyle/models.py":
    dbPath = "/var/log/gilfoyle/database.db"
engine = create_engine(f'sqlite:///{dbPath}')
print(f"DB location: {dbPath}")

Base = declarative_base()

class Gilfoyle(Base):
    __tablename__ = 'gilfoyle'
    id = Column(Integer, primary_key=True)
    sessionId = Column(Integer) # Computer session. All entry bw one boot to one shutdown will have one sessionId
    date = Column(Date)
    time = Column(Time)
    ram = Column(Integer)
    battery = Column(Integer)
    temperature = Column(Integer)
    rpm = Column(Integer)

    # Not used but let it stay
    def to_dict(self):
        return {
            "id": self.id,
            "sessionId": self.sessionId,
            "date": self.date,
            "time": self.time,
            "ram": self.ram,
            "battery": self.battery,
            "temperature": self.temperature,
            "rpm": self.rpm
        }
    
    def __repr__(self):
        return f"Gilfoyle(id={self.id}, sessionId={self.sessionId}, date={self.date}, time={self.time}, ram={self.ram}, battery={self.battery}, temperature={self.temperature}, rpm={self.rpm})"

try:
    Base.metadata.create_all(engine)
except Exception as e:
    print("Failed to connect to DB")
    print(e)
    sys.exit()