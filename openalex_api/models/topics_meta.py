# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  [![Open in](https://img.shields.io/badge/Open%20in-Swagger%20UI-85EA2D?style=for-the-badge&logo=Swagger&link=https://mearman.github.io/openalex-swagger-ui-react/)](https://mearman.github.io/openalex-swagger-ui-react/)  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript)](https://github.com/Mearman/openalex-typescript)  [![TypeScript Fetch](https://img.shields.io/badge/TypeScript%20Fetch-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript-fetch)](https://github.com/Mearman/openalex-typescript-fetch)  [![TypeScript Node](https://img.shields.io/badge/TypeScript%20Node-339933?style=for-the-badge&logo=Node.js&logoColor=white&link=https://github.com/Mearman/openalex-typescript-node)](https://github.com/Mearman/openalex-typescript-node)  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)  ---

    The version of the OpenAPI document: 0.2.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel, Field

class TopicsMeta(BaseModel):
    """
    TopicsMeta
    """
    count: Optional[Any] = Field(...)
    db_response_time_ms: Optional[Any] = Field(...)
    groups_count: Optional[Any] = Field(...)
    page: Optional[Any] = Field(...)
    per_page: Optional[Any] = Field(...)
    __properties = ["count", "db_response_time_ms", "groups_count", "page", "per_page"]

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
    def from_json(cls, json_str: str) -> TopicsMeta:
        """Create an instance of TopicsMeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if count (nullable) is None
        # and __fields_set__ contains the field
        if self.count is None and "count" in self.__fields_set__:
            _dict['count'] = None

        # set to None if db_response_time_ms (nullable) is None
        # and __fields_set__ contains the field
        if self.db_response_time_ms is None and "db_response_time_ms" in self.__fields_set__:
            _dict['db_response_time_ms'] = None

        # set to None if groups_count (nullable) is None
        # and __fields_set__ contains the field
        if self.groups_count is None and "groups_count" in self.__fields_set__:
            _dict['groups_count'] = None

        # set to None if page (nullable) is None
        # and __fields_set__ contains the field
        if self.page is None and "page" in self.__fields_set__:
            _dict['page'] = None

        # set to None if per_page (nullable) is None
        # and __fields_set__ contains the field
        if self.per_page is None and "per_page" in self.__fields_set__:
            _dict['per_page'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TopicsMeta:
        """Create an instance of TopicsMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TopicsMeta.parse_obj(obj)

        _obj = TopicsMeta.parse_obj({
            "count": obj.get("count"),
            "db_response_time_ms": obj.get("db_response_time_ms"),
            "groups_count": obj.get("groups_count"),
            "page": obj.get("page"),
            "per_page": obj.get("per_page")
        })
        return _obj


