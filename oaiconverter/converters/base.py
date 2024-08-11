from typing import TypeVar, Any, Iterable, List
from abc import ABC, abstractmethod

from oaikit import OAIMsg

T_BaseCfgConverterOAI = TypeVar("T_BaseCfgConverterOAI", bound="BaseCfgConverterOAI")
T_BaseConverterOAI = TypeVar("T_BaseConverterOAI", bound="BaseConverterOAI")


class BaseCfgConverterOAI(ABC):
    def __init__(self, *args, **kwargs):
        pass

class BaseConverterOAI:
    def __init__(self, *, cfg: T_BaseCfgConverterOAI):
        self.cfg = cfg

    @abstractmethod
    def msgs2oai(self, *, msgs: Iterable[Any], **kwargs) -> List[OAIMsg]:
        ...
