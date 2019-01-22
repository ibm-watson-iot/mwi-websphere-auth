# Websphere Liberty Authentication
Dockerized Liberty server with OIDC provider

## Overview
Purpose of this server is to provide a bridge between LDAP and a OIDC provider api that can be used as an authorization provider for the Maximo Worker Insights core service.
It is using a Websphere Libery server acting as a OAuth2 provider and OIDC service provider using a LDAP registry as identity provider.
Liberty also supports SAML SSO so it gives us some flexibility depending on what the integration points are with a customer identity provider.

## Configuration
`config/config.xml` contain the configurable part of the image. When writing this it's built into the image, but the intent is that the config directory should be mounted as a kubernetes secret where this file would preside.
### oauthProvider
The oauthProvider section provides the /oauth2 endpoint and here the client is also configured. Multiple clients can be added with different redirection URLs.
### openidConnectProvider
The openidConnectProvider section provides the /oidc endpoint which is an extension to the OAuth2 provider. It's also this endpoint we should be using since it adds the additional JWT generation in an id_token. It also provides the userinfo endpoint which can be used to get user group membership.
### oauth-roles
The OAuth roles are currently set up so that anyone that is authenticated (i.e. is able to login to the LDAP) is also permitted to get a token. This could be restricted to a LDAP group (like a bluegroup).
### ldapRegistry
The ldapRegistry configuration the LDAP registry. 

## iot4i configuration
The oidc endpoints can be used directly with the mwi service. For the mwi api call to /{tenantId}/config/authorization the following format should be used.
```json
{
  "authorizationURL": "https://<hostname><port>/oidc/endpoint/mwi/authorize",
  "tokenURL": "https://<hostname><port>/oidc/endpoint/mwi/token",
  "clientID": "client01",
  "clientSecret": "thisismylittlesecret"
}
```
`mwi` in the URL path is coming from the openidConnectProvider id. cliendID and clientSecret are the ones from config.xml as well.
## mwi logic
The mwi token endpoint must be used to retrieve the access token to be able to authenticate against the mwi service, since it will use the OIDC id_token as access token when passing on. This to be able to only rely on the verification of the HMAC signing of the JWT to allow access instead of having to do a auth server roundtrip to validate the access token.
