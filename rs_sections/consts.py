from django.conf import settings
from django.utils.translation import ugettext_lazy as _

ORDER_BY_PRIORITY = 'priority'
ORDER_BY_PUBDATE = '-pubdate'
ORDER_BY_RANDOM = '?'

ORDER_BY_CHOICES = (
    (ORDER_BY_PRIORITY, _('Priority')),
    (ORDER_BY_PUBDATE, _('Publication Date')),
    (ORDER_BY_RANDOM, _('Random'))
)

# :param: `limit choices to` for possible instances from
# :class:`django.contrib.content_types.models.ContentType`
# possible to include only content_types that are really content
# Example:
# SECTIONS_SECTION_CONTENT_TYPES = {
#   'app_label': 'contents'
# }
SECTION_CONTENT_TYPES = getattr(
    settings,
    'SECTIONS_SECTION_CONTENT_TYPES',
    {}
)

# List of possible naming for sections related
# to special objects
# Example:
# (
#     ('related_topics', 'Related Topics')
# )
SECTION_OBJECT_CHOICES = getattr(
    settings,
    'SECTIONS_SECTION_OBJECT_CHOICES',
    ()
)