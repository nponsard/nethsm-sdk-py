# coding: utf-8
"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from nethsm.client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]
from nethsm.client.shared_imports.server_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]
AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema


@dataclasses.dataclass(frozen=True)
class Host(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    default: typing.Literal["nethsmdemo.nitrokey.com"] = "nethsmdemo.nitrokey.com"


@dataclasses.dataclass(frozen=True)
class Version(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    default: typing.Literal["v1"] = "v1"
Properties = typing.TypedDict(
    'Properties',
    {
        "host": typing.Type[Host],
        "version": typing.Type[Version],
    }
)


class VariablesDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "host",
        "version",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def __new__(
        cls,
        *,
        host: str,
        version: str,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "host": host,
            "version": version,
        }
        used_arg_ = typing.cast(VariablesDictInput, arg_)
        return Variables.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            VariablesDictInput,
            VariablesDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> VariablesDict:
        return Variables.validate(arg, configuration=configuration)
    
    @property
    def host(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("host")
        )
    
    @property
    def version(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("version")
        )
VariablesDictInput = typing.TypedDict(
    'VariablesDictInput',
    {
        "host": str,
        "version": str,
    }
)


@dataclasses.dataclass(frozen=True)
class Variables(
    schemas.Schema[VariablesDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "host",
        "version",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: VariablesDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            VariablesDictInput,
            VariablesDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> VariablesDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass
class Server0(server.ServerWithVariables):
    variables: VariablesDict = dataclasses.field(
        default_factory=lambda: Variables.validate({
            "host": Host.default,
            "version": Version.default,
        })
    )
    variables_schema: typing.Type[Variables] = Variables
    _url: str = "https://{host}/api/{version}"
