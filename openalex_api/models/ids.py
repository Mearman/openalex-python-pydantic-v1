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

class Ids(BaseModel):
    """
    Ids
    """
    crossref: Optional[Any] = None
    doi: Optional[Any] = None
    fatcat: Optional[Any] = None
    grid: Optional[Any] = None
    issn: Optional[Any] = None
    issn_l: Optional[Any] = None
    mag: Optional[Any] = None
    openalex: Optional[Any] = Field(...)
    orcid: Optional[Any] = None
    pmcid: Optional[Any] = None
    pmid: Optional[Any] = None
    ror: Optional[Any] = None
    scopus: Optional[Any] = None
    wikidata: Optional[Any] = None
    wikipedia: Optional[Any] = None
    __properties = ["crossref", "doi", "fatcat", "grid", "issn", "issn_l", "mag", "openalex", "orcid", "pmcid", "pmid", "ror", "scopus", "wikidata", "wikipedia"]

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
    def from_json(cls, json_str: str) -> Ids:
        """Create an instance of Ids from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if crossref (nullable) is None
        # and __fields_set__ contains the field
        if self.crossref is None and "crossref" in self.__fields_set__:
            _dict['crossref'] = None

        # set to None if doi (nullable) is None
        # and __fields_set__ contains the field
        if self.doi is None and "doi" in self.__fields_set__:
            _dict['doi'] = None

        # set to None if fatcat (nullable) is None
        # and __fields_set__ contains the field
        if self.fatcat is None and "fatcat" in self.__fields_set__:
            _dict['fatcat'] = None

        # set to None if grid (nullable) is None
        # and __fields_set__ contains the field
        if self.grid is None and "grid" in self.__fields_set__:
            _dict['grid'] = None

        # set to None if issn (nullable) is None
        # and __fields_set__ contains the field
        if self.issn is None and "issn" in self.__fields_set__:
            _dict['issn'] = None

        # set to None if issn_l (nullable) is None
        # and __fields_set__ contains the field
        if self.issn_l is None and "issn_l" in self.__fields_set__:
            _dict['issn_l'] = None

        # set to None if mag (nullable) is None
        # and __fields_set__ contains the field
        if self.mag is None and "mag" in self.__fields_set__:
            _dict['mag'] = None

        # set to None if openalex (nullable) is None
        # and __fields_set__ contains the field
        if self.openalex is None and "openalex" in self.__fields_set__:
            _dict['openalex'] = None

        # set to None if orcid (nullable) is None
        # and __fields_set__ contains the field
        if self.orcid is None and "orcid" in self.__fields_set__:
            _dict['orcid'] = None

        # set to None if pmcid (nullable) is None
        # and __fields_set__ contains the field
        if self.pmcid is None and "pmcid" in self.__fields_set__:
            _dict['pmcid'] = None

        # set to None if pmid (nullable) is None
        # and __fields_set__ contains the field
        if self.pmid is None and "pmid" in self.__fields_set__:
            _dict['pmid'] = None

        # set to None if ror (nullable) is None
        # and __fields_set__ contains the field
        if self.ror is None and "ror" in self.__fields_set__:
            _dict['ror'] = None

        # set to None if scopus (nullable) is None
        # and __fields_set__ contains the field
        if self.scopus is None and "scopus" in self.__fields_set__:
            _dict['scopus'] = None

        # set to None if wikidata (nullable) is None
        # and __fields_set__ contains the field
        if self.wikidata is None and "wikidata" in self.__fields_set__:
            _dict['wikidata'] = None

        # set to None if wikipedia (nullable) is None
        # and __fields_set__ contains the field
        if self.wikipedia is None and "wikipedia" in self.__fields_set__:
            _dict['wikipedia'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Ids:
        """Create an instance of Ids from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Ids.parse_obj(obj)

        _obj = Ids.parse_obj({
            "crossref": obj.get("crossref"),
            "doi": obj.get("doi"),
            "fatcat": obj.get("fatcat"),
            "grid": obj.get("grid"),
            "issn": obj.get("issn"),
            "issn_l": obj.get("issn_l"),
            "mag": obj.get("mag"),
            "openalex": obj.get("openalex"),
            "orcid": obj.get("orcid"),
            "pmcid": obj.get("pmcid"),
            "pmid": obj.get("pmid"),
            "ror": obj.get("ror"),
            "scopus": obj.get("scopus"),
            "wikidata": obj.get("wikidata"),
            "wikipedia": obj.get("wikipedia")
        })
        return _obj


