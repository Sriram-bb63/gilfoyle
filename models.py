from sqlalchemy import create_engine, Column, Integer, Date, Time, desc
from sqlalchemy.orm import declarative_base


# engine = create_engine('sqlite:////var/log/gilfoyle/database.db')
engine = create_engine('sqlite:///database.db')

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

Base.metadata.create_all(engine)