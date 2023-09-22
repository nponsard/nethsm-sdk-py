# coding: utf-8

"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from nethsm.client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]


from nethsm.client.components.schema import base64
Properties = typing.TypedDict(
    'Properties',
    {
        "encrypted": typing.Type[base64.Base64],
        "iv": typing.Type[base64.Base64],
    }
)


class EncryptDataDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "encrypted",
        "iv",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def __new__(
        cls,
        *,
        encrypted: str,
        iv: str,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "encrypted": encrypted,
            "iv": iv,
        }
        arg_.update(kwargs)
        used_arg_ = typing.cast(EncryptDataDictInput, arg_)
        return EncryptData.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            EncryptDataDictInput,
            EncryptDataDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> EncryptDataDict:
        return EncryptData.validate(arg, configuration=configuration)
    
    @property
    def encrypted(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("encrypted")
        )
    
    @property
    def iv(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("iv")
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
EncryptDataDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class EncryptData(
    schemas.Schema[EncryptDataDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "encrypted",
        "iv",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: EncryptDataDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            EncryptDataDictInput,
            EncryptDataDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> EncryptDataDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

