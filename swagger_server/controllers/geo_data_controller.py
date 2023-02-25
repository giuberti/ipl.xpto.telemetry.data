import connexion
import six
import json
from custom_logging import logging

from models.entities import GeoData
from services.services import GeoDataService
from schemas.schemas import GeoDataSchema
from custom_errors import EntityNotFound, InvalidPayload, BaseCustomError

from swagger_server.models.create_geo_data_request import CreateGeoDataRequest  # noqa: E501
from swagger_server.models.create_geo_data_response import CreateGeoDataResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.error_type_enum import ErrorTypeEnum  # noqa: E501
from swagger_server.models.get_geo_data_response import GetGeoDataResponse  # noqa: E501
from swagger_server.models.list_geo_data_response import ListGeoDataResponse  # noqa: E501
from swagger_server.models.update_geo_data_request import UpdateGeoDataRequest  # noqa: E501
from swagger_server import util


geodata_service = GeoDataService()
geodata_schema = GeoDataSchema()

def create_geo_data(body):  # noqa: E501
    """Create new GeoData

    This operation is used to create a new GeoData on System. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateGeoDataResponse
    """
    logging.info("create_geo_data", body)
    response = None
    response_code = None
    try:
        if not connexion.request.is_json:
            raise InvalidPayload(code="CST002", message="Invalid Request Payload",
                                 details=f"Request payload is not a JSON valid")
        body = CreateGeoDataRequest.from_dict(connexion.request.get_json())  # noqa: E501

        if body.latitude is None or body.longitude is None:
            raise ErrorResponse(code="CST006", message="Invalid Request Payload", type=ErrorTypeEnum.BUSINESS, details=f"Missing required geodata")
        
        entity = GeoData(data_id=None, date_time=body.date_time, vehicle_id=body.vehicle_id, latitude=body.latitude, longitude=body.longitude, altimeter=body.altimeter)
        entity = geodata_service.save(entity)
        response = CreateGeoDataResponse.from_dict(json.loads(geodata_schema.dumps(entity)))
        response_code = 201
    
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CST0002", type=ErrorTypeEnum.PERSISTENCE,
                                 message="Error on create new GeoData", details=str(e))

    return response.to_dict(), response_code


def delete_geo_data(data_id):  # noqa: E501
    """Delete GeoData

    This operation is delete a Data. # noqa: E501

    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data_id = str.from_dict(connexion.request.get_json())  # noqa: E501

    response = None
    response_code = None
    try:
        entity = geodata_service.fetch_by_id(data_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="GeoData not found",
                                 details=f"Unable to find customer ID {data_id}")
        geodata_service.delete(data_id)
        response_code = 204
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CSM999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))
    if response is None:
        return None, response_code
    else:
        return response.to_dict(), response_code

def get_geo_data(data_id):  # noqa: E501
    """Get a single GeoData&#x27;s info

    This operation is used to retrieve the details of a specific device. # noqa: E501

    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: GetGeoDataResponse
    """
    response = None
    response_code = None
    try:
        entity = geodata_service.fetch_by_id(entity_id=data_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="Customer not found",
                                 details=f"Unable to find customer ID {data_id}")
        response = GetGeoDataResponse.from_dict(json.loads(geodata_schema.dumps(entity)))
        response_code = 200
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CSM999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))
    return response.to_dict(), response_code


def list_geo_data():  # noqa: E501
    """Get GeoDatas list

    This operation is used to retrieve a list of GeoDatas. # noqa: E501


    :rtype: ListGeoDataResponse
    """
    entities = geodata_service.fetch_all()

    data_response_list = []
    for entity in entities:
        data_response_list.append(GetGeoDataResponse.from_dict(json.loads(geodata_schema.dumps(entity))))

    response = ListGeoDataResponse(content=data_response_list, total_results=len(data_response_list))
    return response.to_dict(), 200


def update_geo_data(body, data_id):  # noqa: E501
    """Update GeoData&#x27;s attributes

    This operation is used to update some of the GeoData&#x27;s attributes. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: None
    """
    response = None
    response_code = None
    try:
        if not connexion.request.is_json:
            raise InvalidPayload(code="CST002", message="Invalid Request Payload",
                                 details=f"Request payload is not a JSON valid")
        body = UpdateGeoDataRequest.from_dict(connexion.request.get_json())  # noqa: E501
        entity = geodata_service.fetch_by_id(data_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="GeoData not found",
                                 details=f"Unable to find geodata ID {data_id}")
        entity.date_time = body.date_time 
        entity.vehicle_id = body.vehicle_id      
        entity.latitude = body.latitude
        entity.longitude = body.longitude
        entity.altimeter = body.altimeter
        geodata_service.save(entity)
        response_code = 204
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CSM999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))

    if response is None:
        return None, response_code
    else:
        return response.to_dict(), response_code
