#!/usr/bin/env python3
import config
from settings import API_PORT

connex_app = config.connex_app
connex_app.add_api('swagger.yaml', arguments={'title': 'IPL Tracking - Microservice API - Data'}, pythonic_params=True)

with connex_app.app.app_context():
    # Auto-generate a migration
    config.alembic.revision('making changes')

    # Upgrade the database
    config.alembic.upgrade()


if __name__ == '__main__':
    connex_app.run(port=API_PORT, debug=True)
