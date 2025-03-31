#!/bin/bash

TO="le.bosgiraud@gmail.com"
SUBJECT="FestiGo Server Crash Alert"
BODY="The FestiGo server has crashed or the VPS has restarted. The service is being restarted automatically."

# Log the email sending process
echo "Sending email to $TO with subject '$SUBJECT'" >> /tmp/crash-alert.log
echo -e "Subject: $SUBJECT\n\n$BODY" | msmtp "$TO" 2>> /tmp/crash-alert.log

if [ $? -ne 0 ]; then
    echo "Failed to send email. Check /tmp/crash-alert.log for details." >> /tmp/crash-alert.log
else
    echo "Email sent successfully." >> /tmp/crash-alert.log
fi