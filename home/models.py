from django.db import models


class HomeVideo(models.Model):
    vid = models.FileField(upload_to='home/vids', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)


    class Meta:
        verbose_name = 'Home Video'
        verbose_name_plural = 'Home Videos'

    def get_absolute_url(self):
        return reverse('home:video_detail', kwargs={'video_pk': self.pk})