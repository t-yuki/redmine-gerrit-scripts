# Introduction

This is a simple [Gerrit][0] hook for updating [Redmine][1] with information about what changes are made in Gerrit review. Currently two scripts are included that respond to patchset-created and change-merged events. 

When a patchset is created in Gerrit with a project name matching one of the projects defined in config.py its message will be parsed. If the commit message contains a reference to a Redmine issue in the form of #ISSUE_NR an event will be added to the issue history in Redmine. With a link to the patchset in gerrit. If the message contains a link to an issue in the form of #Resolved ISSUE_ID the status in Redmine will be changed to 'Feedback'. In addition to the standard message. 

When a change is merged the commit message is analyzed again. If it contains a link to a Redmine issue in the form of #Resolved ISSUE_ID another message will be added to the issue history in Redmine. Mentioning the name of the submitter for the change, and the status of the issue will be changed to Resolved. 

Script is tested with Redmine 2.4.1 and Gerrit 2.6.1

# Installation

Put the scripts in the `$GERRIT_HOME/hooks` directory and edit the `config.py` script to set several options with project specific values. If gerrit is installed on a Linux server don't forget to make the scripts (`patchset-created` and `change-merged` executable. 

If you want to give the scripts a different name don't forget to correctly set the `[Hooks]` section of the `$GERRIT_HOME/etc/gerrit.config` to include `HOOK_NAME =  new_script_name`. For more information see the gerrit hooks [documentation][2].

# Logging

All print statements are appended to the `$GERRIT_HOME/logs/error_log` file. 

[0]:http://gerrit.googlecode.com
[1]:http://redmine.org
[2]:https://gerrit-review.googlesource.com/Documentation/config-hooks.html
