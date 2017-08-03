#!/usr/bin/python3
from datetime import date
import smtplib
import sys
from email.mime.text import MIMEText

victims = [
  ['Alice', 'alice@test.com'],
  ['Gerardo', 'gerardo@test.com'],
  ['Bob', 'bob@test.com']]
payload = ('Hello {:s},\nThis is a friendly reminder to do some quick cleanup '
  'around the apartment. Just wipe down the counters, sweep the floors, and '
  'touch up anything that looks messy in the common areas and you\'ll be off '
  'the hook for the next 6 weeks.\n -The Chorebot')

def main(argv=sys.argv):
  today = date.today()
  ordinal = (today.month ) * 2
  if today.day > 14:
    ordinal += 1
  victim = ordinal % 3
  name = victims[victim][0]
  print(str(today) + ' - Assigning chores to ' + name)
  address = victims[victim][1]
  msg = MIMEText(payload.format(name))
  msg['From'] = 'chorebot@gcr.me'
  msg['To'] = address
  msg['Subject'] = 'Apartment Cleanup Reminder'
  with smtplib.SMTP() as sender:
    sender.connect()
    sender.send_message(msg)

if __name__ == '__main__':
  main()
