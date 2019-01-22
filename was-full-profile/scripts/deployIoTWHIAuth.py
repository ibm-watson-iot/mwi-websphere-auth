##############################################################################
# Copyright (c) 2019 IBM Corporation and other Contributors.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
##############################################################################
import sys

node = sys.argv[0]
server = sys.argv[1]
war = sys.argv[2]

# Keep track of any errors/exceptions raised during the app installation.
returncode = 0

# Enable OAuth2 provider
print "Enabling WAS OAuth2 provider"
try:
  AdminTask.enableOAuthTAI()
  # Save
  AdminConfig.save()
except:
  _type_, _value_, _tbck_ = sys.exc_info()
  error = `_value_`
  print "Error Installing Application"
  print "Error Message = "+error
  #indicate an error due to an unsuccessful installation
  returncode = 1
#endTry

# Installing Maximo Worker Insights servlet for authentication
try:
  print "Installing Maximo Worker Insights authentication servlet"

  attrs = [
    '-appname', 'iotwhi',
    '-defaultbinding.virtual.host default_host -usedefaultbindings',
    '-node', node,
    '-server', server,
    '-contextroot', '/iotwhi',
    '-MapRolesToUsers [["All Role" No Yes "" ""]]'
  ]
  AdminApp.install(war, attrs)
  AdminConfig.save()
except:
  _type_, _value_, _tbck_ = sys.exc_info()
  error = `_value_`
  print "Error Installing Application"
  print "Error Message = "+error
  #indicate an error due to an unsuccessful installation
  returncode = 2
#endTry

sys.exit(returncode)
