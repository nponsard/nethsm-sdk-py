# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from nethsm.client.shared_imports.response_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .content.application_x_pem_file import schema as application_x_pem_file_schema
from .content.application_xx509_ca_cert import schema as application_xx509_ca_cert_schema
from .content.application_pgp_keys import schema as application_pgp_keys_schema


@dataclasses.dataclass
class ApiResponse(api_response.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        str,
        str,
        str,
    ]
    headers: schemas.Unset = schemas.unset


class ResponseFor200(api_client.OpenApiResponse[ApiResponse]):
    @classmethod
    def get_response(cls, response, headers, body) -> ApiResponse:
        return ApiResponse(response=response, body=body, headers=headers)


    class ApplicationXPemFileMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_x_pem_file_schema.Schema


    class ApplicationXX509CaCertMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_xx509_ca_cert_schema.Schema


    class ApplicationPgpKeysMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_pgp_keys_schema.Schema
    content = {
        'application/x-pem-file': ApplicationXPemFileMediaType,
        'application/x-x509-ca-cert': ApplicationXX509CaCertMediaType,
        'application/pgp-keys': ApplicationPgpKeysMediaType,
    }
