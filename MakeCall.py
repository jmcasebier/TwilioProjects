# Imports
import os, argparse
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Read arguments from command line
parser = argparse.ArgumentParser(description = 'Makes a call, given the URL of the voice file and recipient phone number')
parser.add_argument('-v', '--voice', help = 'URL of the XML voice file', required = True)
parser.add_argument('-r', '--recipient', help = 'Recipient phone number', required = True)
args = parser.parse_args()
print(args.voice)

# Twilio config
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Make call
try:
    call = client.calls.create(
                            url = args.voice,
                            to = args.recipient,
                            from_ = '+1XXXXXXXXXX'
                        )
    print(call.sid)
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
