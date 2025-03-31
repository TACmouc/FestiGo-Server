#!/bin/bash

TO="le.bosgiraud@gmail.com"
SUBJECT="FestiGo Server Crash Alert"
LOG_FILE="/tmp/crash-alert.log"
SERVICE_NAME="festigo-server.service"

# Capture the last 20 lines of the service logs
SERVICE_LOG=$(journalctl -u $SERVICE_NAME -n 20 --no-pager)

BODY="The FestiGo server has crashed or the VPS has restarted. The service is being restarted automatically.

Here are the last logs from the service:
$SERVICE_LOG"

# Log the email sending process
echo "Sending email to $TO with subject '$SUBJECT'" >> $LOG_FILE
echo -e "Subject: $SUBJECT\n\n$BODY" | msmtp "$TO" 2>> $LOG_FILE

if [ $? -ne 0 ]; then
    echo "Failed to send email. Check $LOG_FILE for details." >> $LOG_FILE
else
    echo "Email sent successfully." >> $LOG_FILE
fi