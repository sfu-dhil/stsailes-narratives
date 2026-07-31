from django.db import models
from django.utils.safestring import mark_safe
from django.db.models import Q
from solo.models import SingletonModel

from django_dh_map.models import ContentItem, Map, XyzMap, OverheadImageMap, PanoramaImageMap

class HomePage(SingletonModel):
    first_button_label = models.CharField(verbose_name='First Button Label', default='View Map')
    first_button_map = models.ForeignKey(
        Map,
        null=True,
        related_name='home_page_first_button',
        on_delete=models.CASCADE,
        verbose_name='First Button Map',
        limit_choices_to=Q(published=True),
    )
    second_button_label = models.CharField(verbose_name='Second Button Label', default='View River')
    second_button_map = models.ForeignKey(
        PanoramaImageMap,
        null=True,
        related_name='home_page_second_button',
        on_delete=models.CASCADE,
        verbose_name='Second Button Map',
        limit_choices_to=Q(published=True),
    )

    # relationships
    # one-to-one content_item via HomePageContent Model

    class Meta:
        db_table = 'stsailes_narratives_home_page'
        verbose_name = 'Home Page'

    def __str__(self):
        return 'Home Page'

class HomePageContent(ContentItem):
    # relationships
    home_page = models.OneToOneField(
        HomePage,
        related_name='content_item',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'stsailes_narratives_ci_home_page'
        verbose_name = 'Home Page Content'
