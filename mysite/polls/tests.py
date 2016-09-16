# unit test

from django.test import TestCase
from django.utils import timezone
from polls.models import Poll


class PollModelTest(TestCase):
    def create_poll_and_save_to_db(self):
        # create new poll object with it's question create_poll_and_save_to_db
        poll = Poll()
        poll.question = "What's up?"
        poll.pub_date = timezone.now()

        # check if we can save it to db
        poll.save()

        # look for our poll in the db
        all_polls_in_database = Poll.objects.all()
        self.assertEquals(len(all_polls_in_database), 1)
        only_poll_in_database = all_polls_in_database[0]
        self.assertEquals(only_poll_in_database, poll)

        # check if the attributes: question and pub_date are saved.
        self.assertEquals(only_poll_in_database.question, "What's up?")
        self.assertEquals(only_poll_in_database.pub_date, poll.pub_date)
