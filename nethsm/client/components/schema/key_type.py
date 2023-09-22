# coding: utf-8

"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from nethsm.client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class KeyTypeEnums:

    @schemas.classproperty
    def RSA(cls) -> typing.Literal["RSA"]:
        return KeyType.validate("RSA")

    @schemas.classproperty
    def CURVE25519(cls) -> typing.Literal["Curve25519"]:
        return KeyType.validate("Curve25519")

    @schemas.classproperty
    def EC_P224(cls) -> typing.Literal["EC_P224"]:
        return KeyType.validate("EC_P224")

    @schemas.classproperty
    def EC_P256(cls) -> typing.Literal["EC_P256"]:
        return KeyType.validate("EC_P256")

    @schemas.classproperty
    def EC_P384(cls) -> typing.Literal["EC_P384"]:
        return KeyType.validate("EC_P384")

    @schemas.classproperty
    def EC_P521(cls) -> typing.Literal["EC_P521"]:
        return KeyType.validate("EC_P521")

    @schemas.classproperty
    def GENERIC(cls) -> typing.Literal["Generic"]:
        return KeyType.validate("Generic")


@dataclasses.dataclass(frozen=True)
class KeyType(
    schemas.Schema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "RSA": "RSA",
            "Curve25519": "CURVE25519",
            "EC_P224": "EC_P224",
            "EC_P256": "EC_P256",
            "EC_P384": "EC_P384",
            "EC_P521": "EC_P521",
            "Generic": "GENERIC",
        }
    )
    enums = KeyTypeEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["RSA"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["RSA"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["Curve25519"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["Curve25519"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["EC_P224"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["EC_P224"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["EC_P256"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["EC_P256"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["EC_P384"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["EC_P384"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["EC_P521"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["EC_P521"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["Generic"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["Generic"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["RSA","Curve25519","EC_P224","EC_P256","EC_P384","EC_P521","Generic",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        "RSA",
        "Curve25519",
        "EC_P224",
        "EC_P256",
        "EC_P384",
        "EC_P521",
        "Generic",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                "RSA",
                "Curve25519",
                "EC_P224",
                "EC_P256",
                "EC_P384",
                "EC_P521",
                "Generic",
            ],
            validated_arg
        )
