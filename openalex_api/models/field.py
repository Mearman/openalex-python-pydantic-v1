# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  [![Open in](https://img.shields.io/badge/Open%20in-Swagger%20UI-85EA2D?style=for-the-badge&logo=Swagger&link=https://mearman.github.io/openalex-swagger-ui-react/)](https://mearman.github.io/openalex-swagger-ui-react/)  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript)](https://github.com/Mearman/openalex-typescript)  [![TypeScript Fetch](https://img.shields.io/badge/TypeScript%20Fetch-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript-fetch)](https://github.com/Mearman/openalex-typescript-fetch)  [![TypeScript Node](https://img.shields.io/badge/TypeScript%20Node-339933?style=for-the-badge&logo=Node.js&logoColor=white&link=https://github.com/Mearman/openalex-typescript-node)](https://github.com/Mearman/openalex-typescript-node)  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)  ---

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from openalex_api.models.ids import Ids
from openalex_api.models.topic_level_array_schema import TopicLevelArraySchema
from openalex_api.models.topic_level_schema import TopicLevelSchema

class Field(BaseModel):
    """
    Field
    """
    cited_by_count: StrictInt = Field(...)
    created_date: StrictStr = Field(...)
    description: StrictStr = Field(...)
    display_name: StrictStr = Field(...)
    display_name_alternatives: conlist(StrictStr) = Field(...)
    domain: TopicLevelSchema = Field(...)
    id: StrictStr = Field(...)
    ids: Ids = Field(...)
    siblings: TopicLevelArraySchema = Field(...)
    subfields: TopicLevelArraySchema = Field(...)
    updated_date: StrictStr = Field(...)
    works_api_url: StrictStr = Field(...)
    works_count: StrictInt = Field(...)
    __properties = ["cited_by_count", "created_date", "description", "display_name", "display_name_alternatives", "domain", "id", "ids", "siblings", "subfields", "updated_date", "works_api_url", "works_count"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Field:
        """Create an instance of Field from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of domain
        if self.domain:
            _dict['domain'] = self.domain.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ids
        if self.ids:
            _dict['ids'] = self.ids.to_dict()
        # override the default output from pydantic by calling `to_dict()` of siblings
        if self.siblings:
            _dict['siblings'] = self.siblings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subfields
        if self.subfields:
            _dict['subfields'] = self.subfields.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Field:
        """Create an instance of Field from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Field.parse_obj(obj)

        _obj = Field.parse_obj({
            "cited_by_count": obj.get("cited_by_count"),
            "created_date": obj.get("created_date"),
            "description": obj.get("description"),
            "display_name": obj.get("display_name"),
            "display_name_alternatives": obj.get("display_name_alternatives"),
            "domain": TopicLevelSchema.from_dict(obj.get("domain")) if obj.get("domain") is not None else None,
            "id": obj.get("id"),
            "ids": Ids.from_dict(obj.get("ids")) if obj.get("ids") is not None else None,
            "siblings": TopicLevelArraySchema.from_dict(obj.get("siblings")) if obj.get("siblings") is not None else None,
            "subfields": TopicLevelArraySchema.from_dict(obj.get("subfields")) if obj.get("subfields") is not None else None,
            "updated_date": obj.get("updated_date"),
            "works_api_url": obj.get("works_api_url"),
            "works_count": obj.get("works_count")
        })
        return _obj


