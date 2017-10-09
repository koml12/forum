from django.db import models
from django.urls import reverse
import datetime
import uuid


class ForumPostManager(models.Manager):
    """
    Class that manages operations involving the 'ForumPost' model
    """
    @staticmethod
    def create_post(text, link):
        time = datetime.datetime.now()
        post = ForumPost(post_text=text, post_link=link, post_date=time)
        return post


class ForumPost(models.Model):

    # Fields
    post_text = models.CharField(max_length=200, help_text="Title for the post, typically a description of the URL")
    post_link = models.URLField(max_length=200, default='', help_text="Link to the post's content")
    post_date = models.DateTimeField(help_text="Date and time that the post was submitted")
    votes = models.IntegerField(default=0, help_text="Number of votes for the post")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    # Methods
    def __str__(self):
        """
        String representation of a ForumPost object
        :return: text field of the post
        """
        return self.post_text

    def get_absolute_url(self):
        return reverse('forumposts:forumpost-detail', args=[str(self.pk)])

    def was_posted_long_ago(self):
        """
        Checks if a post was created greater than certain "unit" lengths of time (i.e. year, month, day)
        Usage: to help format the way the post date is displayed to the user.
        
        :return: A dict containing boolean values for "year", "month", "week", "day", and "hour".
                 Interpretation: if long_ago['year'] == True, the post was created 1 or more years ago, and so on for
                 other time units
        """
        long_ago = {'year': False, 'week': False, 'day': False, 'hour': False}
        today_date = datetime.datetime.now()

        # Check for more than a year
        year_delta = datetime.timedelta(days=365)
        if today_date - self.post_date > year_delta:
            long_ago['year'] = True
            return long_ago

        # Check for more than a week
        week_delta = datetime.timedelta(weeks=1)
        if today_date - self.post_date > week_delta:
            long_ago['week'] = True
            return long_ago

        # Check for more than a day
        day_delta = datetime.timedelta(days=1)
        if today_date - self.post_date >= day_delta:
            long_ago['day'] = True
            return long_ago

        # Check for more than an hour
        hour_delta = datetime.timedelta(hours=1)
        if today_date - self.post_date > hour_delta:
            long_ago['hour'] = True
            return long_ago

        return long_ago


class CommentManager(models.Manager):
    """
    Class that manages operations related to the 'Comment' model.
    """
    @staticmethod
    def add_comment(post, text):
        time = datetime.datetime.now()
        comment = Comment(text=text, post=post, date_time=time)
        return comment


class Comment(models.Model):
    """
    Class representing a comment on a forum post.
    """
    # Fields
    text = models.TextField(max_length=10000, help_text='Comment for a particular forum post')
    post = models.ForeignKey('ForumPost', on_delete=models.SET_NULL, null=True)
    date_time = models.DateTimeField(default=None, null=True)

    def __str__(self):
        """
        String representation of a comment.
        :return: The post the comment is made in reference to, and the text of the comment.
        """
        return self.post.post_text + '->' + self.text
