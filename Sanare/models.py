from django.db import models
from datetime import datetime


class LovePost(models.Model):
    sender_id = models.CharField(max_length=30)
    sender_name = models.CharField(max_length=30, default="")
    receiver_id = models.CharField(max_length=30)
    pub_date = models.DateTimeField('published', default=datetime.now)
    receiver_name = models.CharField(max_length=30, default="")
    is_old = models.BooleanField('outdated', default=False)

    def explain_is_old(self):
        if self.is_old:
            return "Old Love"
        else:
            return "Current Love"

    def __unicode__(self):
        return self.sender_id + " to " + self.receiver_id + " at " + str(self.pub_date) + " : " + self.explain_is_old()

    def to_display(self):
        return "You sent love to " + self.receiver_name + " at " + str(self.pub_date.strftime("%Y-%m-%d %H:%M")) + " : " + self.explain_is_old()


class MatchedPair(models.Model):
    id1 = models.CharField(max_length=30)
    id2 = models.CharField(max_length=30)
    name1 = models.CharField(max_length=30, default="")
    name2 = models.CharField(max_length=30, default="")
    pub_date = models.DateTimeField('published', default=datetime.now)

    def __unicode__(self):
        return self.id1 + " and " + self.id2 + " at " + str(self.pub_date)

    def get_partner_name(self):
        return self.name2

    def to_display(self):
        return "Successful Love with " + self.name1 + " and " + self.name2 + " at " + str(self.pub_date.strftime("%Y-%m-%d %H:%M"))

    def to_display_just_matched(self):
        return "Just successfully matched with " + self.name1 + " and " + self.name2 + " at " + str(self.pub_date.strftime("%Y-%m-%d %H:%M"))
