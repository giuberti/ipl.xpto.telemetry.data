# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.enum_sensor_type import EnumSensorType  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class GetTelemetryDataResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data_id: str=None, vehicle_id: str=None, date_time: str=None, type: EnumSensorType=None, value: float=None):  # noqa: E501
        """GetTelemetryDataResponse - a model defined in Swagger

        :param data_id: The data_id of this GetTelemetryDataResponse.  # noqa: E501
        :type data_id: str
        :param vehicle_id: The vehicle_id of this GetTelemetryDataResponse.  # noqa: E501
        :type vehicle_id: str
        :param date_time: The date_time of this GetTelemetryDataResponse.  # noqa: E501
        :type date_time: str
        :param type: The type of this GetTelemetryDataResponse.  # noqa: E501
        :type type: EnumSensorType
        :param value: The value of this GetTelemetryDataResponse.  # noqa: E501
        :type value: float
        """
        self.swagger_types = {
            'data_id': str,
            'vehicle_id': str,
            'date_time': str,
            'type': EnumSensorType,
            'value': float
        }

        self.attribute_map = {
            'data_id': 'data_id',
            'vehicle_id': 'vehicle_id',
            'date_time': 'date_time',
            'type': 'type',
            'value': 'value'
        }
        self._data_id = data_id
        self._vehicle_id = vehicle_id
        self._date_time = date_time
        self._type = type
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'GetTelemetryDataResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetTelemetryDataResponse of this GetTelemetryDataResponse.  # noqa: E501
        :rtype: GetTelemetryDataResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_id(self) -> str:
        """Gets the data_id of this GetTelemetryDataResponse.


        :return: The data_id of this GetTelemetryDataResponse.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id: str):
        """Sets the data_id of this GetTelemetryDataResponse.


        :param data_id: The data_id of this GetTelemetryDataResponse.
        :type data_id: str
        """
        if data_id is None:
            raise ValueError("Invalid value for `data_id`, must not be `None`")  # noqa: E501

        self._data_id = data_id

    @property
    def vehicle_id(self) -> str:
        """Gets the vehicle_id of this GetTelemetryDataResponse.


        :return: The vehicle_id of this GetTelemetryDataResponse.
        :rtype: str
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id: str):
        """Sets the vehicle_id of this GetTelemetryDataResponse.


        :param vehicle_id: The vehicle_id of this GetTelemetryDataResponse.
        :type vehicle_id: str
        """
        if vehicle_id is None:
            raise ValueError("Invalid value for `vehicle_id`, must not be `None`")  # noqa: E501

        self._vehicle_id = vehicle_id

    @property
    def date_time(self) -> str:
        """Gets the date_time of this GetTelemetryDataResponse.

        Date and Time of Data  # noqa: E501

        :return: The date_time of this GetTelemetryDataResponse.
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time: str):
        """Sets the date_time of this GetTelemetryDataResponse.

        Date and Time of Data  # noqa: E501

        :param date_time: The date_time of this GetTelemetryDataResponse.
        :type date_time: str
        """
        if date_time is None:
            raise ValueError("Invalid value for `date_time`, must not be `None`")  # noqa: E501

        self._date_time = date_time

    @property
    def type(self) -> EnumSensorType:
        """Gets the type of this GetTelemetryDataResponse.


        :return: The type of this GetTelemetryDataResponse.
        :rtype: EnumSensorType
        """
        return self._type

    @type.setter
    def type(self, type: EnumSensorType):
        """Sets the type of this GetTelemetryDataResponse.


        :param type: The type of this GetTelemetryDataResponse.
        :type type: EnumSensorType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def value(self) -> float:
        """Gets the value of this GetTelemetryDataResponse.

        Value readed by telemetry  # noqa: E501

        :return: The value of this GetTelemetryDataResponse.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value: float):
        """Sets the value of this GetTelemetryDataResponse.

        Value readed by telemetry  # noqa: E501

        :param value: The value of this GetTelemetryDataResponse.
        :type value: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value
