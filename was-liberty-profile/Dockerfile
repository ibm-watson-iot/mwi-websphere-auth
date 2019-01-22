FROM websphere-liberty:kernel

# Pre-install some features to save build time when config file is changed
RUN featureManager install openidConnectServer-1.0 appSecurity-2.0 ldapRegistry-3.0 localConnector-1.0 ssl-1.0 oauth-2.0 --when-file-exists=ignore --acceptLicense

RUN featureManager install adminCenter-1.0 --when-file-exists=ignore --acceptLicense

COPY server.xml /config/
# TODO: expect as volume instead
COPY config/config.xml /config/config/

RUN installUtility install --acceptLicense defaultServer

EXPOSE 9080 9443
