# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "monitor log-analytics solution create",
)
class Create(AAZCommand):
    """Create the Solution.

    :example: Create a log-analytics solution of type Containers
        az monitor log-analytics solution create --resource-group MyResourceGroup --solution-type Containers --tags key=value --workspace "/subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/ Microsoft.OperationalInsights/workspaces/{WorkspaceName}"
    """

    _aaz_info = {
        "version": "2015-11-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.operationsmanagement/solutions/{}", "2015-11-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the log-analytics solution. It should be in the format of solutionType(workspaceName). SolutionType part is case sensitive.",
            required=True,
        )
        _args_schema.location = AAZResourceLocationArg(
            help="Resource location",
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.plan = AAZObjectArg(
            options=["--plan"],
            help="Plan for solution object supported by the OperationsManagement resource provider.",
        )
        _args_schema.workspace_id = AAZStrArg(
            options=["--workspace-id"],
            help="The azure resourceId for the workspace where the solution will be deployed/enabled.",
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="Space-separated tags: key[=value] [key[=value] ...]. Use \"\" to clear existing tags.",
        )

        plan = cls._args_schema.plan
        plan.name = AAZStrArg(
            options=["name"],
            help="name of the solution to be created. For Microsoft published solution it should be in the format of solutionType(workspaceName). SolutionType part is case sensitive. For third party solution, it can be anything.",
        )
        plan.product = AAZStrArg(
            options=["product"],
            help="name of the solution to enabled/add. For Microsoft published gallery solution it should be in the format of OMSGallery/<solutionType>. This is case sensitive",
        )
        plan.promotion_code = AAZStrArg(
            options=["promotion-code"],
            help="promotionCode, Not really used now, can you left as empty",
        )
        plan.publisher = AAZStrArg(
            options=["publisher"],
            help="Publisher name. For gallery solution, it is Microsoft.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.SolutionsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class SolutionsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationsManagement/solutions/{solutionName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "solutionName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2015-11-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("plan", AAZObjectType, ".plan")
            _builder.set_prop("properties", AAZObjectType)
            _builder.set_prop("tags", AAZDictType, ".tags")

            plan = _builder.get(".plan")
            if plan is not None:
                plan.set_prop("name", AAZStrType, ".name")
                plan.set_prop("product", AAZStrType, ".product")
                plan.set_prop("promotionCode", AAZStrType, ".promotion_code")
                plan.set_prop("publisher", AAZStrType, ".publisher")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("workspaceResourceId", AAZStrType, ".workspace_id", typ_kwargs={"flags": {"required": True}})

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_201
            )

        _schema_on_201 = None

        @classmethod
        def _build_schema_on_201(cls):
            if cls._schema_on_201 is not None:
                return cls._schema_on_201

            cls._schema_on_201 = AAZObjectType()

            _schema_on_201 = cls._schema_on_201
            _schema_on_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_201.location = AAZStrType()
            _schema_on_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_201.plan = AAZObjectType()
            _schema_on_201.properties = AAZObjectType()
            _schema_on_201.tags = AAZDictType()
            _schema_on_201.type = AAZStrType(
                flags={"read_only": True},
            )

            plan = cls._schema_on_201.plan
            plan.name = AAZStrType()
            plan.product = AAZStrType()
            plan.promotion_code = AAZStrType(
                serialized_name="promotionCode",
            )
            plan.publisher = AAZStrType()

            properties = cls._schema_on_201.properties
            properties.contained_resources = AAZListType(
                serialized_name="containedResources",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.referenced_resources = AAZListType(
                serialized_name="referencedResources",
            )
            properties.workspace_resource_id = AAZStrType(
                serialized_name="workspaceResourceId",
                flags={"required": True},
            )

            contained_resources = cls._schema_on_201.properties.contained_resources
            contained_resources.Element = AAZStrType()

            referenced_resources = cls._schema_on_201.properties.referenced_resources
            referenced_resources.Element = AAZStrType()

            tags = cls._schema_on_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]