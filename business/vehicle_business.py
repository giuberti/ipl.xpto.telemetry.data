import requests
import logging
from settings import API_VEHICLE_URL
import uuid

class VehicleBusiness:

    def verify (uuid):
        logging.info('Verify_vehicle')
        result = False
        url = API_VEHICLE_URL + '/' + uuid
        logging.info(url)
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            logging.info(data)
            result = True
        else:
            logging.warning(f'Error: {response.status_code}')

        return result

