import django.contrib.gis.db.models
import django.db.models

class Downloaded(django.contrib.gis.db.models.Model):
    objects = django.contrib.gis.db.models.GeoManager()
    src = django.db.models.CharField(max_length=128, null=False, blank=False)
    filename = django.db.models.CharField(max_length=1024, null=False, blank=False)
    datetime = django.db.models.DateTimeField(blank=True, null=True)

    parent = django.db.models.ForeignKey("Downloaded", blank=True, null=True, related_name="children")

    class Meta:
        unique_together = ('src', 'parent', 'filename',)

    def save(self, *args, **kwargs):
        if not self.datetime:
            self.datetime = datetime.datetime.today()
        super(Downloaded, self).save(*args, **kwargs)
