"""
This template is written by @Edhim
What does this quickstart script aim to do?
- I am using simple settings for my personal account with a crontab each 3H,
it's been working since 5 months with no problem.
"""

from instapy import InstaPy
from instapy.util import smart_run
import time


# get a session!
session = InstaPy(username='bundmotivation', password='IedvinaS1234')




with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=False,
                                    potency_ratio=-1.21,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    max_following=5555,
                                    min_followers=45,
                                    min_following=77)
    session.set_do_comment(True, percentage=50)
    session.set_comments(['aMazing!Follow me!', 'So cool!Could you follow me!', 'Nice!', 'wow looks nice!',
                          'this is awesome!'])

    # activity
    session.like_by_tags(
        ['love', 'instagood', 'photooftheday', 'fashion', 'beautiful', 'happy', 'cute', 'tbt', 'like4like', 'followme',
         'picoftheday', 'follow', 'me'],
        amount=8, skip_top_posts=True)

    


client.run(str(os.environ.get('BOT_TOKEN')))
