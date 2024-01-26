# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  [![Open in](https://img.shields.io/badge/Open%20in-Swagger%20UI-85EA2D?style=for-the-badge&logo=Swagger&link=https://mearman.github.io/openalex-swagger-ui-react/)](https://mearman.github.io/openalex-swagger-ui-react/)  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript)](https://github.com/Mearman/openalex-typescript)  [![TypeScript Fetch](https://img.shields.io/badge/TypeScript%20Fetch-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript-fetch)](https://github.com/Mearman/openalex-typescript-fetch)  [![TypeScript Node](https://img.shields.io/badge/TypeScript%20Node-339933?style=for-the-badge&logo=Node.js&logoColor=white&link=https://github.com/Mearman/openalex-typescript-node)](https://github.com/Mearman/openalex-typescript-node)  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)  ---

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openalex_api_pydantic_v1.models.work_schema import WorkSchema  # noqa: E501

class TestWorkSchema(unittest.TestCase):
    """WorkSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkSchema:
        """Test WorkSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkSchema`
        """
        model = WorkSchema()  # noqa: E501
        if include_optional:
            return WorkSchema(
                abstract_inverted_index = None,
                apc_list = openalex_api_pydantic_v1.models.apc.apc(
                    currency = null, 
                    provenance = null, 
                    value = null, 
                    value_usd = null, ),
                apc_paid = openalex_api_pydantic_v1.models.apc.apc(
                    currency = null, 
                    provenance = null, 
                    value = null, 
                    value_usd = null, ),
                authorships = None,
                best_oa_location = openalex_api_pydantic_v1.models.location.location(
                    is_accepted = null, 
                    is_oa = null, 
                    is_published = null, 
                    landing_page_url = null, 
                    license = null, 
                    pdf_url = null, 
                    source = openalex_api_pydantic_v1.models.location_source.location_source(
                        display_name = null, 
                        host_organization = null, 
                        host_organization_lineage = null, 
                        host_organization_lineage_names = null, 
                        host_organization_name = null, 
                        id = null, 
                        is_in_doaj = null, 
                        is_oa = null, 
                        issn = null, 
                        issn_l = null, 
                        type = null, ), 
                    version = null, ),
                biblio = openalex_api_pydantic_v1.models.work_schema_biblio.workSchema_biblio(
                    first_page = null, 
                    issue = null, 
                    last_page = null, 
                    volume = null, ),
                cited_by_api_url = None,
                cited_by_count = None,
                cited_by_percentile_year = openalex_api_pydantic_v1.models.work_schema_cited_by_percentile_year.workSchema_cited_by_percentile_year(
                    max = null, 
                    min = null, ),
                concepts = None,
                corresponding_author_ids = None,
                corresponding_institution_ids = None,
                countries_distinct_count = None,
                counts_by_year = None,
                created_date = None,
                display_name = None,
                doi = None,
                grants = None,
                has_fulltext = None,
                id = None,
                ids = openalex_api_pydantic_v1.models.ids.ids(
                    crossref = null, 
                    doi = null, 
                    fatcat = null, 
                    grid = null, 
                    issn = null, 
                    issn_l = null, 
                    mag = null, 
                    openalex = null, 
                    orcid = null, 
                    pmcid = null, 
                    pmid = null, 
                    ror = null, 
                    scopus = null, 
                    wikidata = null, 
                    wikipedia = null, ),
                institutions_distinct_count = None,
                is_paratext = None,
                is_retracted = None,
                keywords = None,
                language = None,
                locations = None,
                locations_count = None,
                mesh = None,
                ngrams_url = None,
                open_access = openalex_api_pydantic_v1.models.work_schema_open_access.workSchema_open_access(
                    any_repository_has_fulltext = null, 
                    is_oa = null, 
                    oa_status = null, 
                    oa_url = null, ),
                primary_location = openalex_api_pydantic_v1.models.location.location(
                    is_accepted = null, 
                    is_oa = null, 
                    is_published = null, 
                    landing_page_url = null, 
                    license = null, 
                    pdf_url = null, 
                    source = openalex_api_pydantic_v1.models.location_source.location_source(
                        display_name = null, 
                        host_organization = null, 
                        host_organization_lineage = null, 
                        host_organization_lineage_names = null, 
                        host_organization_name = null, 
                        id = null, 
                        is_in_doaj = null, 
                        is_oa = null, 
                        issn = null, 
                        issn_l = null, 
                        type = null, ), 
                    version = null, ),
                publication_date = None,
                publication_year = None,
                referenced_works = None,
                referenced_works_count = None,
                related_works = None,
                sustainable_development_goals = None,
                title = None,
                type = None,
                type_crossref = None,
                updated_date = None
            )
        else:
            return WorkSchema(
                display_name = None,
                id = None,
        )
        """

    def testWorkSchema(self):
        """Test WorkSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()