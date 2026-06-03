from pydantic import BaseModel
class SourceConfig(BaseModel): path: str
class SinkConfig(BaseModel): path: str
