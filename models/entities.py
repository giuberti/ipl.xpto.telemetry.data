from sqlalchemy.orm import relationship
from config import db
from sqlalchemy.dialects.postgresql import UUID

import uuid

class EnumSensorType:
    ODOMETER = "ODOMETER"
    RPM = "RPM"
    SPEED = "SPEED"

class GeoData(db.Model):

    __tablename__ = "geoDatas"

    data_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehicle_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, unique=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    altimeter = db.Column(db.Float, nullable=True)

    def __init__(self, data_id, date_time, vehicle_id, latitude, longitude, altimeter):
        self.data_id = data_id
        self.date_time = date_time
        self.vehicle_id = vehicle_id
        self.latitude = latitude
        self.longitude = longitude
        self.altimeter = altimeter

    def get_id(self):
        return self.data_id
    
    def __repr__(self):
        return 'GeoData(data_id=%d, date_time=%s, vehicle_id=%s, latitude=%s, longitude=%s, altimeter=%s)' % (self.data_id, self.date_time, self.vehicle_id, self.latitude, self.longitude, self.altimeter)
    
    def json(self):
         return {'data_id': str(self.data_id), 'date_time': self.date_time, 'vehicle_id': self.vehicle_id, 'latitude': self.latitude, 'longitude': self.longitude, 'altimeter': self.altimeter}

class TelemetryData(db.Model):
    __tablename__ = "telemetryDatas"
    
    data_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehicle_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, unique=False)
    type = db.Column(db.String, nullable=True)
    value = db.Column(db.Float, nullable=True)

    def __init__(self, data_id, date_time, vehicle_id, type, value):
        self.data_id = data_id
        self.date_time = date_time
        self.vehicle_id = vehicle_id
        self.type = type
        self.value = value

    def get_id(self):
        return self.data_id
    
    def __repr__(self):
        return 'TelemetryData(data_id=%d, date_time=%s, vehicle_id=%s, type=%s, value=%s)' % (self.data_id, self.date_time, self.vehicle_id, self.type, self.value)
    
    def json(self):
        return {'data_id': str(self.data_id), 'date_time': self.date_time, 'vehicle_id': self.vehicle_id, 'type': str(self.type), 'value': self.value}
