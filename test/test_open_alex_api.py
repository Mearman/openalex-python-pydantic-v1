# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  [![Open in](https://img.shields.io/badge/Open%20in-Swagger%20UI-85EA2D?style=for-the-badge&logo=Swagger&link=https://mearman.github.io/openalex-swagger-ui-react/)](https://mearman.github.io/openalex-swagger-ui-react/)  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript)](https://github.com/Mearman/openalex-typescript)  [![TypeScript Fetch](https://img.shields.io/badge/TypeScript%20Fetch-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript-fetch)](https://github.com/Mearman/openalex-typescript-fetch)  [![TypeScript Node](https://img.shields.io/badge/TypeScript%20Node-339933?style=for-the-badge&logo=Node.js&logoColor=white&link=https://github.com/Mearman/openalex-typescript-node)](https://github.com/Mearman/openalex-typescript-node)  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)  ---

    The version of the OpenAPI document: 0.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openalex_api.api.open_alex_api import OpenAlexApi  # noqa: E501


class TestOpenAlexApi(unittest.TestCase):
    """OpenAlexApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OpenAlexApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_author(self) -> None:
        """Test case for get_author

        Get Author  # noqa: E501
        """
        pass

    def test_get_authors(self) -> None:
        """Test case for get_authors

        List Authors  # noqa: E501
        """
        pass

    def test_get_autocomplete(self) -> None:
        """Test case for get_autocomplete

        /autocomplete  # noqa: E501
        """
        pass

    def test_get_autocomplete_authors(self) -> None:
        """Test case for get_autocomplete_authors

        /autocomplete/authors  # noqa: E501
        """
        pass

    def test_get_autocomplete_concepts(self) -> None:
        """Test case for get_autocomplete_concepts

        /autocomplete/concepts  # noqa: E501
        """
        pass

    def test_get_autocomplete_funders(self) -> None:
        """Test case for get_autocomplete_funders

        /autocomplete/funders  # noqa: E501
        """
        pass

    def test_get_autocomplete_institutions(self) -> None:
        """Test case for get_autocomplete_institutions

        /autocomplete/institutions  # noqa: E501
        """
        pass

    def test_get_autocomplete_publishers(self) -> None:
        """Test case for get_autocomplete_publishers

        /autocomplete/publishers  # noqa: E501
        """
        pass

    def test_get_autocomplete_sources(self) -> None:
        """Test case for get_autocomplete_sources

        /autocomplete/sources  # noqa: E501
        """
        pass

    def test_get_autocomplete_works(self) -> None:
        """Test case for get_autocomplete_works

        /autocomplete/works  # noqa: E501
        """
        pass

    def test_get_concept_by_id(self) -> None:
        """Test case for get_concept_by_id

        /concepts/{id}  # noqa: E501
        """
        pass

    def test_get_concepts(self) -> None:
        """Test case for get_concepts

        /concepts  # noqa: E501
        """
        pass

    def test_get_domain_by_id(self) -> None:
        """Test case for get_domain_by_id

        /domains/{id}  # noqa: E501
        """
        pass

    def test_get_field_by_id(self) -> None:
        """Test case for get_field_by_id

        /fields/{id}  # noqa: E501
        """
        pass

    def test_get_funder(self) -> None:
        """Test case for get_funder

        /funders/{id}  # noqa: E501
        """
        pass

    def test_get_funders(self) -> None:
        """Test case for get_funders

        /funders  # noqa: E501
        """
        pass

    def test_get_institution(self) -> None:
        """Test case for get_institution

        /institutions/{id}  # noqa: E501
        """
        pass

    def test_get_institutions(self) -> None:
        """Test case for get_institutions

        /institutions  # noqa: E501
        """
        pass

    def test_get_person(self) -> None:
        """Test case for get_person

        /people/{id}  # noqa: E501
        """
        pass

    def test_get_publisher(self) -> None:
        """Test case for get_publisher

        /publishers/{id}  # noqa: E501
        """
        pass

    def test_get_publishers(self) -> None:
        """Test case for get_publishers

        /publishers  # noqa: E501
        """
        pass

    def test_get_random_author(self) -> None:
        """Test case for get_random_author

        Get Random Author  # noqa: E501
        """
        pass

    def test_get_random_concept(self) -> None:
        """Test case for get_random_concept

        /concepts/random  # noqa: E501
        """
        pass

    def test_get_random_funder(self) -> None:
        """Test case for get_random_funder

        /funders/random  # noqa: E501
        """
        pass

    def test_get_random_institution(self) -> None:
        """Test case for get_random_institution

        /institutions/random  # noqa: E501
        """
        pass

    def test_get_random_publisher(self) -> None:
        """Test case for get_random_publisher

        /publishers/random  # noqa: E501
        """
        pass

    def test_get_random_source(self) -> None:
        """Test case for get_random_source

        /sources/random  # noqa: E501
        """
        pass

    def test_get_random_work(self) -> None:
        """Test case for get_random_work

        /works/random  # noqa: E501
        """
        pass

    def test_get_root(self) -> None:
        """Test case for get_root

        Root  # noqa: E501
        """
        pass

    def test_get_source(self) -> None:
        """Test case for get_source

        /sources/{id}  # noqa: E501
        """
        pass

    def test_get_sources(self) -> None:
        """Test case for get_sources

        /sources  # noqa: E501
        """
        pass

    def test_get_subfield_by_id(self) -> None:
        """Test case for get_subfield_by_id

        /subfields/{id}  # noqa: E501
        """
        pass

    def test_get_topic_by_id(self) -> None:
        """Test case for get_topic_by_id

        /topics/{id}  # noqa: E501
        """
        pass

    def test_get_topics(self) -> None:
        """Test case for get_topics

        /topics  # noqa: E501
        """
        pass

    def test_get_work(self) -> None:
        """Test case for get_work

        /works/{id}  # noqa: E501
        """
        pass

    def test_get_work_ngrams(self) -> None:
        """Test case for get_work_ngrams

        /works/{id}/ngrams  # noqa: E501
        """
        pass

    def test_get_works(self) -> None:
        """Test case for get_works

        /works  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
