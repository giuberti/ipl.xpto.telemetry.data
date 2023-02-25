from flask_marshmallow.fields import fields

from config import ma
from models.entities import GeoData, TelemetryData
from typing import List


class GeoDataSchema(ma.SQLAlchemyAutoSchema):
    dataId = fields.String(attribute="data_id")

    class Meta:
        model = GeoData
        load_instance = True
        exclude = ["data_id"]

class TelemetryDataSchema(ma.SQLAlchemyAutoSchema):
    dataId = fields.String(attribute="data_id")

    class Meta:
        model = TelemetryData
        load_instance = True
        exclude = ["data_id"]
