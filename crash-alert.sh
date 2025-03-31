#!/bin/bash

TO="le.bosgiraud@gmail.com"
SUBJECT="FestiGo Server Crash Alert"
BODY="The FestiGo server has crashed or the VPS has restarted. The service is being restarted automatically."

echo "$BODY" | mail -s "$SUBJECT" "$TO"
