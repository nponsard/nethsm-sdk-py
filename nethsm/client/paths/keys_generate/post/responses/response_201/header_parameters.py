# coding: utf-8

"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from pynitrokey.nethsm.client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from pynitrokey.nethsm.client.paths.keys_generate.post.responses.response_201.headers.header_location import schema
Properties = typing.TypedDict(
    'Properties',
    {
        "location": typing.Type[schema.Schema],
    }
)


class HeadersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "location",
    })
    
    def __new__(
        cls,
        *,
        location: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key, val in (
            ("location", location),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        used_arg_ = typing.cast(HeadersDictInput, arg_)
        return Headers.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            HeadersDictInput,
            HeadersDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> HeadersDict:
        return Headers.validate(arg, configuration=configuration)
    
    @property
    def location(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("location", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
HeadersDictInput = typing.TypedDict(
    'HeadersDictInput',
    {
        "location": str,
    },
    total=False
)


@dataclasses.dataclass(frozen=True)
class Headers(
    schemas.Schema[HeadersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: HeadersDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            HeadersDictInput,
            HeadersDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> HeadersDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

