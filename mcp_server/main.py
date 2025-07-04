# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T15:34:24+00:00



import argparse
import json
import os
from typing import *

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity, UnsuportedSecurityStub

from models import UserResponse

app = MCPProxy(
    contact={'name': 'eBay Inc,', 'x-twitter': 'ebay'},
    description='<span class="tablenote"><b>Note:</b> Not all the account related fields are returned for an authenticated user. The fields returned in the response are controlled by the scopes and are available only to select developers approved by business units.</span><br /><br />Retrieves the authenticated user\'s account profile information. It can be used to let users log into your app or site using eBay, which frees you from needing to store and protect user\'s PII (Personal Identifiable Information) data.',
    license={
        'name': 'eBay API License Agreement',
        'url': 'https://go.developer.ebay.com/api-license-agreement',
    },
    title='Identity API',
    version='v1.1.0',
    servers=[
        {
            'description': 'Production',
            'url': 'https://apiz.ebay.com{basePath}',
            'variables': {'basePath': {'default': '/commerce/identity/v1'}},
        }
    ],
)


@app.get(
    '/user/',
    description=""" This method retrieves the account profile information for an authenticated user, which requires a User access token. What is returned is controlled by the scopes. For a business account you use the default scope commerce.identity.readonly, which returns all the fields in the businessAccount container. These are returned because this is all public information. For an individual account, the fields returned in the individualAccount container are based on the scope you use. Using the default scope, only public information, such as eBay user ID, are returned. For details about what each scope returns, see the Identity API Overview. URLs for this method Production URL: https://apiz.ebay.com/commerce/identity/v1/user/ Sandbox URL: https://apiz.sandbox.ebay.com/commerce/identity/v1/user/ In the Sandbox, this method returns mock data. Note: You must use the correct scope or scopes for the data you want returned. """,
    tags=['user_profile_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_user():
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
