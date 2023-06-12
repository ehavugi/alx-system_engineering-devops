# My first postmortem
This post-mortem report is for refers Web stack debugging Project incident
where apache server started returning 500 errors at Jun 5, 
2023 9:00 PM MST. We understand the issues impact ALX  systems 
using wordpress and its secondary users. 
## Issue Summary 
From 9:00  PM to 11:00pm MST, the requests 127.0.0.1:80 were returning HTTP 500 errors.

The issue was found and fixed, by 11:00 PM, endpoint was returning status code 200. 

## Timeline
+ 9:00 PM: server configuration was updated
+ 9:05 PM: DataDog webmonitor detected large number of 500 Errors
+ 9:10 PM: Engineers on Call was alerted of the continued issue
+ 9:40 PM: Engineers had figured out the issue severity and called for help
+ 10:10 PM: Team on fixed issues on select servers and starting working on automating fix
+ 10:30 PM: Team had written puppet script and roll the fix across infrastructure
+ 11:00 PM: Systems back to normal levels of traffic and all status normal.
# Root cause and resolution

+ The configuration had an error in a specific file reference which cause the process to stop unfinished
+ The filename had a .phpp extension instead of .php and hence couldn't be located
+ The error was found and file extension fixed.

# Corrective and preventative measures
+ Store previous configuration version and autoreload old one if new configuration fail for minor changes
+ Add more checks by introducing a sandbox to test new configuration before release to entire infrastructure
+ 