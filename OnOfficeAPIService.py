import hmac
import base64
import hashlib
from BaseAPIService import BaseAPIService

from models import RequestAction, RequestData, RequestRoot


class OnOfficeService():
    ACTION_ID_GET = "urn:onoffice - de - ns: smart:2.5: smartml:action: get"
    ACTION_ID_READ = "urn:onoffice-de-ns:smart:2.5:smartml:action:read"
    ACTION_ID_DO = "urn:onoffice - de - ns: smart:2.5: smartml:action: do"
    ACTION_ID_EDIT = "urn:onoffice - de - ns: smart:2.5: smartml:action: modify"
    ACTION_ID_CREATE = "urn:onoffice - de - ns: smart:2.5: smartml:action: create"
    ACTION_ID_DELETE = "urn:onoffice - de - ns: smart:2.5: smartml:action: delete"

    RELATION_TYPE_BUYER = 'urn:onoffice-de-ns:smart:2.5:relationTypes:estate:address:buyer'
    RELATION_TYPE_TENANT = 'urn:onoffice-de-ns:smart:2.5:relationTypes:estate:address:renter'
    RELATION_TYPE_OWNER = 'urn:onoffice-de-ns:smart:2.5:relationTypes:estate:address:owner'
    RELATION_TYPE_CONTACT_BROKER = 'urn:onoffice-de-ns:smart:2.5:relationTypes:estate:address:contactPerson'
    RELATION_TYPE_CONTACT_PERSON = 'urn:onoffice-de-ns:smart:2.5:relationTypes:estate:address:contactPersonAll'
    RELATION_TYPE_COMPLEX_ESTATE_UNITS = 'urn:onoffice-de-ns:smart:2.5:relationTypes:complex:estate:units'
    RELATION_TYPE_ESTATE_ADDRESS_OWNER = 'urn:onoffice-de-ns:smart:2.5:relationTypes:estate:address:owner'

    MODULE_ADDRESS = 'address'
    MODULE_ESTATE = 'estate'
    MODULE_SEARCHCRITERIA = 'searchcriteria'

    def __init__(self, base_url, api_token):
        self.base_url = base_url
        self.api_token = api_token

    @staticmethod
    def generate_hmac(token, secret, timestamp, resource_type, action_id):

        fields = f"{timestamp}{token}{resource_type}{action_id}"
        hmac_hash = hmac.new(secret.encode('utf-8'), fields.encode('utf-8'), hashlib.sha256).digest()
        return base64.b64encode(hmac_hash).decode('utf-8')


    def get_estates(self, params=None, resource_id: str = ""):
        action = RequestAction(
            actionId=OnOfficeService.ACTION_ID_READ,
            resourceId=resource_id,
            resourceType=OnOfficeService.MODULE_ESTATE,
            identifier="",
            parameters=params,
            hmac="sss"
        )
        request_data = RequestData(actions=[action])
        payload = RequestRoot(token=self.api_token, request=request_data)

        print(payload.model_dump_json())


off = OnOfficeService("someti", "some")
print(off.get_estates())
