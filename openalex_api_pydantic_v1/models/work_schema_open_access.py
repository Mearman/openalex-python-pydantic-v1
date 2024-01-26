# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  [![Open in](https://img.shields.io/badge/Open%20in-Swagger%20UI-85EA2D?style=for-the-badge&logo=Swagger&link=https://mearman.github.io/openalex-swagger-ui-react/)](https://mearman.github.io/openalex-swagger-ui-react/)  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript)](https://github.com/Mearman/openalex-typescript)  [![TypeScript Fetch](https://img.shields.io/badge/TypeScript%20Fetch-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript-fetch)](https://github.com/Mearman/openalex-typescript-fetch)  [![TypeScript Node](https://img.shields.io/badge/TypeScript%20Node-339933?style=for-the-badge&logo=Node.js&logoColor=white&link=https://github.com/Mearman/openalex-typescript-node)](https://github.com/Mearman/openalex-typescript-node)  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)  ---

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel, Field

class WorkSchemaOpenAccess(BaseModel):
    """
    WorkSchemaOpenAccess
    """
    any_repository_has_fulltext: Optional[Any] = Field(...)
    is_oa: Optional[Any] = Field(...)
    oa_status: Optional[Any] = Field(...)
    oa_url: Optional[Any] = Field(...)
    __properties = ["any_repository_has_fulltext", "is_oa", "oa_status", "oa_url"]

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
    def from_json(cls, json_str: str) -> WorkSchemaOpenAccess:
        """Create an instance of WorkSchemaOpenAccess from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if any_repository_has_fulltext (nullable) is None
        # and __fields_set__ contains the field
        if self.any_repository_has_fulltext is None and "any_repository_has_fulltext" in self.__fields_set__:
            _dict['any_repository_has_fulltext'] = None

        # set to None if is_oa (nullable) is None
        # and __fields_set__ contains the field
        if self.is_oa is None and "is_oa" in self.__fields_set__:
            _dict['is_oa'] = None

        # set to None if oa_status (nullable) is None
        # and __fields_set__ contains the field
        if self.oa_status is None and "oa_status" in self.__fields_set__:
            _dict['oa_status'] = None

        # set to None if oa_url (nullable) is None
        # and __fields_set__ contains the field
        if self.oa_url is None and "oa_url" in self.__fields_set__:
            _dict['oa_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WorkSchemaOpenAccess:
        """Create an instance of WorkSchemaOpenAccess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WorkSchemaOpenAccess.parse_obj(obj)

        _obj = WorkSchemaOpenAccess.parse_obj({
            "any_repository_has_fulltext": obj.get("any_repository_has_fulltext"),
            "is_oa": obj.get("is_oa"),
            "oa_status": obj.get("oa_status"),
            "oa_url": obj.get("oa_url")
        })
        return _obj


