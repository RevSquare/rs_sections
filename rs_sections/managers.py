from django.contrib.contenttypes.models import ContentType
from django.db import models


class ContentTypeQuerySet(models.QuerySet):

    def _get_ct(self, obj):
        """
        :param obj: register django model
        :return: ContentType for model
        """
        return ContentType.objects.get_for_model(obj.__class__)


class SectionQuerySet(ContentTypeQuerySet):
    """
    QuerySet to section model :class: sections.models.Section
    will be used as manager to it
    """

    def get_by_system_name(self, slug):
        """
        :param slug: string
        :return: Section :class:sections.models.Section instance
        """
        return self.get(system_name=slug)

    def main_sections(self, system_names=None):
        """
        List of sections not related to object
        :param system_names: list of system names
        :return: queryset
        """
        queryset = self.filter(content_type__isnull=True)
        if system_names:
            queryset = queryset.filter(system_name__in=system_names)
        return queryset

    def object_sections(self, obj=None):
        """
        Llist of sections related to objects only
        :return: queryset
        """
        if obj is None:
            return self.filter(content_type__isnull=False)
        else:
            ct = self._get_ct(obj)
            return self.filter(content_type=ct, object_id=obj.pk)


class SectionItemQuerySet(ContentTypeQuerySet):
    """
    Queryset for :class: `sections.models.SectionItem`
    will be used as manager
    """

    def for_object(self, obj):
        """
        return all section items related to given obj

        :param obj: register django model
        :return: queryset
        """

        ct = self._get_ct(obj)
        return self.filter(
            content_type=ct,
            object_id=obj.pk
        )
