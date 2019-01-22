# WAS Full profile OAuth2 provider for mwi
## Introduction
Instructions on how to set up an OAuth2 provider in a WAS Full Profile installation so that it can be used by mwi service for authentication.

Since WAS full profile does not provide a OIDC provider like WAS liberty profile, strictly OAuth2 is used. To be able to support token validation and getting information from user registry, a servlet is deployed that will provide a OIDC userinfo endpoint.

## Websphere Instructions

1. Stop the server
2. Navigate to the `app_server_root/bin` directory.
3. Run the command: ```
  wsadmin -conntype NONE -f
installOAuth2Service.py install <nodeName> <serverName>
-profileName <profileName>```
4. Upon completion, the command should give this message: `ADMA5013I: Application WebSphereOauth20SP installed successfully.`
5. Navigate to the `<was_profile_root>/config/cells/<cell_name>` directory.
6. An oauth20 subfolder is used at this location to store the OAuth configuration. If the folder does not exist in your deployment, create it: `<was_profile_root>/config/cells/<cell_name>/oauth20`.
7. Copy the files `base.clients.xml` and `IoTWHI.xml` to the `oauth20` directory. base.clients.xml can be updated with other client credentials.
8. Run the command: `wsadmin -conntype NONE -f deployIoTWHIAuth.py install <nodeName> <serverName> <path to iotwhi.war>`
9. Start the server

## Maximo Worker Insights Instructions
1. Open up the swagger UI for the tenant (https://iotworkerinsights.ibm.com/docs/#/authorization/putAuthorizationServer)
2. Make a PUT call on the /authorization endpoint with the following content (replace the clientSecret with what you have selected in the configuration file):
```
{
  "authorizationURL": "<websphere host>/oauth2/endpoint/IoTWHI/authorize",
  "tokenURL": "<websphere host>/oauth2/endpoint/IoTWHI/token",
  "userinfoURL": "<websphere host>/iotwhi/userinfo",
  "clientID": "client01",
  "clientSecret": "thisismylittlesecret"
}
```
