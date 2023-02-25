import connexion
import six
import json
from custom_logging import logging

from models.entities import TelemetryData
from services.services import TelemetryDataService
from schemas.schemas import TelemetryDataSchema
from custom_errors import EntityNotFound, InvalidPayload, BaseCustomError

from swagger_server.models.create_telemetry_data_request import CreateTelemetryDataRequest  # noqa: E501
from swagger_server.models.create_telemetry_data_response import CreateTelemetryDataResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.error_type_enum import ErrorTypeEnum  # noqa: E501
from swagger_server.models.get_telemetry_data_response import GetTelemetryDataResponse  # noqa: E501
from swagger_server.models.list_telemetry_data_response import ListTelemetryDataResponse  # noqa: E501
from swagger_server.models.update_telemetry_data_request import UpdateTelemetryDataRequest  # noqa: E501
from swagger_server import util

telemetrydata_service = TelemetryDataService()
telemetrydata_schema = TelemetryDataSchema()

def create_telemetry_data(body):  # noqa: E501
    """Create new TelemetryData

    This operation is usedto create a new Data on System. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateTelemetryDataResponse
    """
    logging.info("create_telemetry_data")
    response = None
    response_code = None
    try:
        if not connexion.request.is_json:
            raise InvalidPayload(code="CST002", message="Invalid Request Payload",
                                 details=f"Request payload is not a JSON valid")
        body = CreateTelemetryDataRequest.from_dict(connexion.request.get_json())  # noqa: E501
        
        entity = TelemetryData(data_id=None, date_time=body.date_time, vehicle_id=body.vehicle_id, type=body.type, value=body.value)
        entity = telemetrydata_service.save(entity)
        response = CreateTelemetryDataResponse.from_dict(json.loads(telemetrydata_schema.dumps(entity)))
        response_code = 201
    
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CST0002", type=ErrorTypeEnum.PERSISTENCE,
                                 message="Error on create new TelemetryData", details=str(e))

    return response.to_dict(), response_code


def delete_telemetry_data(data_id):  # noqa: E501
    """Delete TelemetryData

    This operation is delete a TelemetryData. # noqa: E501

    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data_id = str.from_dict(connexion.request.get_json())  # noqa: E501

    response = None
    response_code = None
    try:
        entity = telemetrydata_service.fetch_by_id(data_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="TelemetryData not found",
                                 details=f"Unable to find TelemetryData ID {data_id}")
        telemetrydata_service.delete(data_id)
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



def get_telemetry_data(data_id):  # noqa: E501
    """Get a single TelemetryData&#x27;s info

    This operation is used to retrieve the details of a specific device. # noqa: E501

    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: GetTelemetryDataResponse
    """
    response = None
    response_code = None
    try:
        entity = telemetrydata_service.fetch_by_id(entity_id=data_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="TelemetryData not found",
                                 details=f"Unable to find TelemetryData ID {data_id}")
        response = GetTelemetryDataResponse.from_dict(json.loads(telemetrydata_schema.dumps(entity)))
        response_code = 200
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CSM999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))
    return response.to_dict(), response_code


def list_telemetry_data():  # noqa: E501
    """Get TelemetryData list

    This operation is used to retrieve a list of Datas. # noqa: E501


    :rtype: ListTelemetryDataResponse
    """
    entities = telemetrydata_service.fetch_all()

    data_response_list = []
    for entity in entities:
        data_response_list.append(GetTelemetryDataResponse.from_dict(json.loads(telemetrydata_schema.dumps(entity))))

    response = ListTelemetryDataResponse(content=data_response_list, total_results=len(data_response_list))
    return response.to_dict(), 200


def update_telemetry_data(body, data_id):  # noqa: E501
    """Update TelemetryData&#x27;s attributes

    This operation is used to update some of the Data&#x27;s attributes. # noqa: E501

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
        body = UpdateTelemetryDataRequest.from_dict(connexion.request.get_json())  # noqa: E501
        entity = telemetrydata_service.fetch_by_id(data_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="TelemetryData not found",
                                 details=f"Unable to find TelemetryData ID {data_id}")
        entity.date_time = body.date_time 
        entity.vehicle_id = body.vehicle_id      
        entity.type = body.type
        entity.value = body.value
        telemetrydata_service.save(entity)
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
