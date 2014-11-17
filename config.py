#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Nathan Cassee
#

# set your API key here. You can find it under "My account" in Redmine, i.e. http://redmine.mydomain.com/my/account
REDMINE_API_KEY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# the hostname or ip number of redmine, do not include the port number here.
REDMINE_HOST = "redmine.mydomain.com"

# The port number on which redmine is listening, change this to 443 if the
# redmine host is using a secure connection
REDMINE_HOST_PORT_NUMBER = 80

# Set this to true if the redmine host is using a secure connection (SSL)
REDMINE_HOST_USING_SSL = False

# if you want the script to update the status of the issue in redmine
# you'll need to set this to the id number of that status. otherwise set
# it to None and it won't update the status

# the regex we use for findig the issue id
REDMINE_ISSUE_ID_REGEX = '\#(\d+)'

# Matches both #Resolved 5 as #Resolves 5
REDMINE_RESOLVED_ISSUE_REGEX = '\#Resolve[ds] (\d+)'

# which gerrit projects to run the script for
GERRIT_PROJECTS = ["PROJECT_NAME"]
