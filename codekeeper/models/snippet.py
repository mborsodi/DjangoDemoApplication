from codekeeper.models import tag
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import post_delete

class Snippet(models.Model):
    class Meta:
        app_label = "codekeeper"

    title = models.CharField(max_length=256, blank=True, null=True)
    snippet = models.TextField()

    tags = models.ManyToManyField("codekeeper.Tag")
    creator = models.ForeignKey("codekeeper.Person")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}".format(self.title)


@receiver(post_save, sender=Snippet)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import scorched
    print ("Hello")


    solrconn = scorched.SolrInterface(settings.SOLR_SERVER)
    records = solrconn.query(type="snippet", item_id="{0}".format(instance.pk)).execute()
    if records:
        solrconn.delete_by_ids([x['id'] for x in records])

    d = {
        "id": str(uuid.uuid4()),
        "type": "snippet",
        "item_id": instance.pk,
        "snippet": instance.snippet,
        "title": instance.title,
        #"tags": [tag.name for tag in instance.tags.all()]
    }

    solrconn.add(d)
    solrconn.commit()


@receiver(post_delete, sender=Snippet)
def solr_del(instance, **kwargs):
    from django.conf import settings
    import scorched
    solrconn = scorched.SolrInterface(settings.SOLR_SERVER)
    records = solrconn.query(type="snippet", item_id="{0}".format(instance.pk)).execute()
    if records:
        solrconn.delete_by_ids([x['id'] for x in records])

    solrconn.commit()