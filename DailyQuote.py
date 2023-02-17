# Imports
from random import randint
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Daily Quotes
quotes = ["You are never too old to set another goal or dream a new dream.\n-CS Lewis",
"Think big when you set your goals. Dare to think big and then set a series of smaller goals to get you there.\n-Les Brown"
"Goals should never be easy, they should force you to work, even if they are uncomfortable at the time.\n-Michael Phelps",
"If you want to be happy, set a goal that commands your thoughts, liberates your energy, and inspires your hopes.\n-Andrew Carnegie",
"What you get by achieving your goals is not as important as what you become by achieving your goals.\n-Zig Ziglar",
"Goals help you channel your energy into action.\n-Les Brown",
"Motivation is what gets you started. Habit is what keeps you going.\n-Jim Rohn",
"To sit on an idea or fail to act on a goal is not really goal-setting, but wishful thinking.\n-Les Brown",
"Do or do not, there is no try.\n-Yoda",
"Start now. Start where you are. Start with fear. Start with pain. Start with doubt. Start with your hands shaking. Just start.\n-Mel Robbins",
"Get a good idea and stay with it. Do it, and work at it until it's done right.\n-Walt Disney",
"It isn't what you do, but how you do it.\n-John Wooden",
"Don't wait. The time will never be just right.\n-Napoleon Hill",
"We are what we repeatedly do. Excellence, then, is not an act, but a habit.\n-Aristotle",
"The difference between ordinary and extraordinary is that little extra.\n-Jimmy Johnson",
"The way to get started is to quit talking and begin doing.\n-Walt Disney",
"Done is better than perfect.\n-Sheryl Sandberg",
"Do what you can with all you have, wherever you are.\n-Theodore Roosevelt",
"Anyone can do something when they want to do it. Really successful people do things when they don't want to do it.\n-Dr Phil",
"Persevere and get it done.\n-George Allen Sr",
"The most important things in life aren't things.\n-Anthony D'Angelo",
"Owning less is better than organizing more.\n-Joshua Becker",
"Owning less is great, wanting less is better.\n-Joshua Becker",
"Enjoy all you have while pursuing all you want.\n-Jim Rohn",
"If I cannot do great things, I can do small things in a great way.\n-Martin Luther King Jr",
"Every morning is a fresh start. Wake up with a thankful heart.\n-Kristen Butler",
"We tend to get what we expect.\n-Norman Vincent Peale",
"When you're curious, you find lots of interesting things to do.\n-Walt Disney",
"We delight in the beauty of the butterfly, but rarely admit the changes it has gone through to achieve that beauty.\n-Maya Angelou",
"Experience is what you get when you don't get what you want.-Dan Stanford",
"Even the greatest was once a beginner. Don't be afraid to take that first step.\n-Muhammad Ali",
"The distance is nothing; it's only the first step that is difficult.\n-Marquise du Deffand",
"Logic gets you from A to B, imagination gets you anywhere.\n-Albert Einstein",
"Only a mediocre person is always at his best.\n-W Somerset Maugham",
"Simplify. Remove steps. Remove options. Remove instructions. Remove clutter.\n-Gabor Cselle",
"Those that can, do. Those that can't, complain.\n-Linus Torvalds",
"Knowing what you need to do to improve your life takes wisdom. Pushing yourself to do it takes courage.\n-Mel Robbins",
"Don't mistake activity with achievement.\n-John Wooden",
"Creativity is allowing yourself to make mistakes. Art is knowing which ones to keep.\n-Scott Adams",
"There are two mistakes one can make along the road to truth: not going all the way, and not starting.\n-Buddha",
"Don't worry about failures, worry about the chances you miss when you don't even try.\n-Jack Canfield",
"There are two ways to get enough. One is to continue to accumulate more and more. The other is to desire less.\n-GK Chesterton",
"You cannot soar with the eagles as long as you hang out with the turkeys.\n-Joel Osteen",
"You will never change what you tolerate.\n-Joel Osteen",
"There is no right time, there is only right now.\n-Mel Robbins",
"Nobody can go back and start a new beginning, but anyone can start today and make a new ending.\n-Maria Robinson",
"Even the strongest blizzards start with a single snowflake.\n-Sara Raasch"
"An obstacle is often a stepping stone.\n-William Prescott",
"Keep your face to the sunshine and you cannot see a shadow.\n-Helen Keller",
"Success is getting what you want. Happiness is wanting what you get.\n-Dale Carnegie",
"Successful people are simply those with successful habits.\n-Brian Tracy",
"Success is the sum of small efforts repeated day in and day out.\n-Robert Collier",
"It is our attitude at the beginning of a difficult task which, more than anything else, will affect its successful outcome.\n-William James",
"A year from now you may wish you had started today.\n-Karen Lamb",
"Don't make excuses, don't blame the past. The rest of your life can be the best of your life.\n-Joel Osteen",
"If there is no struggle, there is no progress.\n-Frederick Douglass",
"The scariest moment is always just before you start.\n-Stephen King",
"The harder I work, the luckier I get.\n-Gary Player",
"A flower does not think of competing with the flower next to it. It just blooms.\n-Zen Shin",
"To plant a garden is to believe in tomorrow.\n-Audrey Hepburn",
"Every flower must grow through dirt.\n-Laurie Jean Sennott",
"Success is not final, failure is not fatal; it is the courage to continue that counts.\n-Winston Churchill",
"The path to success is to take massive, determined action.\n-Tony Robbins",
"The road to success is dotted with many tempting parking spaces.\n-Will Rogers",
"Some people dream of success, while others wake up and work hard at it.\n-Mark Zuckerberg",
"For success, attitude is equally as important as ability.\n-Harry F Banks",
"Failure is the condiment that gives success its flavor.\n-Truman Capote",
"Success is going from failure to failure without losing enthusiasm.\n-Winston Churchill",
"There are no mistakes or failures, only lessons.\n-Denis Waitley",
"The only way to do great work is to love what you do.\n-Steve Jobs",
"The question isn't who is going to let me, it's who is going to stop me.\n-Ayn Rand",
"In the middle of difficulty lies opportunity.\n-Albert Einstein",
"There is only one thing that makes a dream impossible to achieve: the fear of failure.\n-Paulo Coelho",
"Learn to be calm and you will always be happy.\n-Paramahansa Yogananda",
"Anyone who doesn't make mistakes isn't working hard enough.\n-Wes Roberts",
"You always pass failure on the way to success.\n-Mickey Rooney",
"The only real mistake is the one from which we learn nothing.\n-John Powell",
"Always do your best. What you plant now, you will harvest later.\n-Og Mandino",
"The greatest mistake you can make in life is to be continually fearing that you will make one.\n-Elbert Hubbard",
"Don't find fault, find a remedy.\n-Henry Ford",
"Mistakes are the stairs we climb to reach success.\n-Tim Fargo",]

# Twilio config
account_sid = '%'
auth_token = '%'
client = Client(account_sid, auth_token)

# Message information
recipients = ['+1XXXXXXXXXX',]
message = quotes[randint(0, len(quotes) - 1)]

# Send the messages
for recipient in recipients:
    try:
        sms = client.messages.create(
            to = recipient, 
            messaging_service_sid = '%',
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