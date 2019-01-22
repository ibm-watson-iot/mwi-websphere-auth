##############################################################################
# Copyright (c) 2019 IBM Corporation and other Contributors.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
##############################################################################

FROM websphere-liberty:kernel

# Pre-install some features to save build time when config file is changed
RUN featureManager install openidConnectServer-1.0 appSecurity-2.0 ldapRegistry-3.0 localConnector-1.0 ssl-1.0 oauth-2.0 --when-file-exists=ignore --acceptLicense

RUN featureManager install adminCenter-1.0 --when-file-exists=ignore --acceptLicense

COPY server.xml /config/
# TODO: expect as volume instead
COPY config/config.xml /config/config/

RUN installUtility install --acceptLicense defaultServer

EXPOSE 9080 9443
