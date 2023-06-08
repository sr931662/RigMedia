from django.db import models

# Create your models here.


# class RedditCommentItem(models.Model):
#     id = models.IntegerField(db_index=True, primary_key=True)
#     pwc_upload = models.TextField()
#     cop_upload = models.TextField()
#     pwc_links = models.TextField()
#     pwc_headlines = models.TextField()
#     pwc_upvotes = models.TextField()
#     pwc_comments = models.TextField()
#     pwc_rewards = models.TextField()
#     cop_upvotes = models.TextField()
#     cop_rewards = models.TextField()
#     comment = models.TextField()
#
#     objects = models.Manager()
#
#     def __str__(self):
#         return f"""Id : {self.id}\n Post Upload time : {self.pwc_upload}\n Comment Upload time : {self.cop_upload}\n
# Post Links : {self.pwc_links}\n Post headlines : {self.pwc_headlines}\n Post Upvotes : {self.pwc_upvotes}\n
# Post comment : {self.pwc_comments}\n Post rewards : {self.pwc_rewards}\n Comment Upvotes : {self.cop_upvotes}\n
# Comment rewards : {self.cop_rewards}\n Comment Body : {self.comment}"""


class RedditPostDataItem(models.Model):
    id = models.IntegerField(db_index=True, primary_key=True)
    post_upload = models.TextField()
    post_headline = models.TextField(null=True)
    post_upvotes = models.TextField()
    post_comments = models.TextField()
    post_rewards = models.TextField()
    post_page_links = models.TextField()
    redditor = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.id, self.post_upload, self.post_headline, self.post_upvotes, self.post_comments, self.post_rewards, self.post_page_links