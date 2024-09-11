import time
from datetime import datetime

from pydantic import BaseModel
from typing import List, Dict, Optional


class RequestAction(BaseModel):
    hmac: str
    actionId: str
    hmac_version: int = 2
    resourceId: Optional[str] = ""
    identifier: Optional[str] = ""
    resourceType: Optional[str] = ""
    parameters: Optional[Dict[str, str]]
    timestamp: Optional[datetime] = int(time.time())


class RequestData(BaseModel):
    actions: List[RequestAction]


class RequestRoot(BaseModel):
    token: str
    request: RequestData
