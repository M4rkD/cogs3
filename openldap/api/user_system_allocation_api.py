import jsonschema
import logging
import requests

from django.conf import settings

from openldap import schemas
from openldap.decorators import OpenLDAPException
from openldap.util import decode_response

logger = logging.getLogger('openldap')


@OpenLDAPException(logger)
def get_system_allocation(email):
    """
    Get a system allocation.

    Args:
        email (str): User's email address - required
    """
    raise NotImplementedError('Not yet implemented.')


@OpenLDAPException(logger)
def update_system_allocation(email, system_id):
    """
    Update a system allocation.

    Args:
        email (str): User's email address - required
        system_id (str): System name [hawk, sunbird].
    """
    raise NotImplementedError('Not yet implemented.')


@OpenLDAPException(logger)
def delete_system_allocation(email, system_id):
    """
    Delete a system allocation.

    Args:
        email (str): User's email address - required
        system_id (str): System name [hawk, sunbird].
    """
    raise NotImplementedError('Not yet implemented.')
