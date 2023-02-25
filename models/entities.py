from sqlalchemy.orm import relationship

from config import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

import uuid

class EnumSensorType:
    ODOMETER = "ODOMETER"
    RPM = "RPM"
    SPEED = "SPEED"

class Data(db.Model):

    data_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehicle_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, unique=False)
    
    def get_id(self):
        return self.data_id

    def __init__(self, data_id, date_time, vehicle_id):
        self.data_id = data_id
        self.date_time = date_time
        self.vehicle_id = vehicle_id

class GeoData(Data):

    __tablename__ = "geoDatas"

    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    altimeter = db.Column(db.Float, nullable=True)

    def __init__(self, data_id, date_time, vehicle_id, latitude, longitude, altimeter):
        super().__init__(self, data_id, date_time, vehicle_id)
        self.latitude = latitude
        self.longitude = longitude
        self.altimeter = altimeter

    def json(self):
         return {'data_id': str(self.data_id), 'date_time': self.date_time, 'vehicle_id': self.vehicle_id, 'latitude': self.latitude, 'longitude': self.longitude, 'altimeter': self.altimeter}

class TelemetryData(Data):
    __tablename__ = "telemetryDatas"

    type = db.Column(db.String, nullable=True)
    value = db.Column(db.Float, nullable=True)

    def __init__(self, data_id, date_time, vehicle_id, type, value):
        super().__init__(self, data_id, date_time, vehicle_id)
        self.type = type
        self.value = value

    def json(self):
        return {'data_id': str(self.data_id), 'date_time': self.date_time, 'vehicle_id': self.vehicle_id, 'type': str(self.type), 'value': self.value}
