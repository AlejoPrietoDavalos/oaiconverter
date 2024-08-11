from typing import List

from oaikit import OAIMsg
from wapchita import WapChat

from oaiconverter.converters.base import BaseConverterOAI, BaseCfgConverterOAI


class CfgWapOAI(BaseCfgConverterOAI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ConverterWapOAI(BaseConverterOAI):
    def __init__(self, *, cfg: BaseCfgConverterOAI):
        super().__init__(cfg=cfg)
    
    def msgs2oai(self, *, msgs: List[WapChat]) -> List[OAIMsg]:
        return super().msgs2oai(msgs=msgs)
