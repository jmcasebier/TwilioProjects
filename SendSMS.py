# Imports
import os, argparse
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Read arguments from command line
parser = argparse.ArgumentParser(description = 'Sends an SMS message, given the message body and recipient phone number(s)')
parser.add_argument('-m', '--message', help = 'Text value of SMS message body', required = True)
parser.add_argument('-r', '--recipients', help = 'Comma separated list of recipient phone number(s)', required = True)
args = parser.parse_args()

# Twilio config
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Message information
to_numbers = [r.strip() for r in args.recipients.split(',')]
message = args.message.strip()

# Send the messages
for to_number in to_numbers:
    try:
        sms = client.messages.create(
            to = to_number, 
            messaging_service_sid = os.environ['TWILIO_MESSAGING_SERVICE_SID'],
            body = message)
        print(sms.sid)
    except TwilioRestException as err:
        print(err)

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#         000  0000000000    000000000    #
#         000  00000000000  00000000      #
#         001  001 001 001  100           #
#         101  101 101 101  101           #
#         110  011 110 010  101           #
#         101  101  10 101  101           #
#         111  111   1 111  111           #
#    111  111  111     111  111           #
#    111 1 11  111     11    111 111 1    #
#     1 111     1      1      1 11 11     #
#                                         #
#          http://jmcasebier.com          #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #