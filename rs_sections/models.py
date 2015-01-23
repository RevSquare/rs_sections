import logging
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .consts import ORDER_BY_CHOICES, ORDER_BY_PRIORITY, SECTION_CONTENT_TYPES
from .managers import SectionQuerySet, SectionItemQuerySet

logger = logging.getLogger(__name__)


class SectionAbstract(models.Model):
    """
    Section Name, Model that will allow us to group elements in the
    section

    :param:`name` Section Name
    :param:`system_name` System name used to get sections in various of
    queries and templatetags. Should be unique
    :param:`limit` Limit of news in the section ( More news can be assigned
    but only this amount of news will be displayed)
    :param:`order_by` chosen order in section
    :param:`content_types` possible content type to chose in SectionItem
    :param:`content_type` possible to relate section with specific content_type
    :param:`object_id` object_id for selected content_type
    """

    name = models.CharField(_('Name'), max_length=255)
    system_name = models.SlugField(_('System Name'), max_length=255)

    limit = models.PositiveSmallIntegerField(_('Limit'), default=5)
    order_by = models.CharField(_('Order by'), choices=ORDER_BY_CHOICES,
        default=ORDER_BY_PRIORITY, max_length=20)

    content_types = models.ManyToManyField(ContentType, null=True, blank=True,
        limit_choices_to=SECTION_CONTENT_TYPES)

    content_type = models.ForeignKey(ContentType, null=True, blank=True,
        related_name='section_content_type')
    object_id = models.PositiveIntegerField(null=True, blank=True)

    content_object = GenericForeignKey('content_type', 'object_id')
    objects = SectionQuerySet.as_manager()

    class Meta:
        abstract = True
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')

    def __unicode__(self):
        if self.content_type and self.object_id:
            return u'%s: %s' % (self.name, unicode(self.content_object))
        else:
            return self.name



class SectionItemAbstract(models.Model):
    """
    Single Item in a section abstract class,
    pls extend this and add custom fields that you want to store over here
    """


    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(_('Object Id'))

    priority = models.PositiveIntegerField(_('Priority'), default=0)
    pubdate = models.DateTimeField(_('Pub Date'), auto_now_add=True)

    content_object = GenericForeignKey('content_type', 'object_id')

    objects = SectionItemQuerySet.as_manager()

    class Meta:
        abstract = True
        verbose_name = _('Section Item')
        verbose_name_plural = _('Section Items')
        ordering = ('priority',)

    def save(self, *args, **kwargs):
        """
        Move data from content_object to section_item so we
        don't need to do additional query
        """
        ct = kwargs.pop('ct', None)
        self.setup_section_item_data(ct=ct)
        super(SectionItemAbstract, self).save(*args, **kwargs)

    def setup_section_item_data(self):
        """
        setup data from content_object to SectionItem to prevent
        additional queries
        """
        pass

    def ready(self):
        pass

    @classmethod
    def update_section_item(self, sender, instance, **kwargs):
        """
        Update Section item after save content
        """
        section_items = self.objects.for_object(instance)
        for section_item in section_items:
            section_item.save(ct=instance)

        def __unicode__(self):
            return unicode(self.content_object)

    @classmethod
    def remove_section_item(self, sender, instance, *args, **kwargs):
        """
        Remove all related SectionItem instances
        :param sender:
        :param instance:
        :param using:
        :param kwargs:
        :return:
        """
        section_items = self.objects.for_object(instance)
        for section_item in section_items:
            section_item.delete()

