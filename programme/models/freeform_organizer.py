# encoding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _


class FreeformOrganizer(models.Model):
    """
    Not all programme-organizing entities are natural Persons. Programme might be attributed to,
    for example, companies, non-profit associations or informal groups of people such as convention
    committees.
    """

    programme = models.ForeignKey('programme.Programme',
        verbose_name=_(u'Programme'),
        related_name='freeform_organizers',
    )

    text = models.CharField(
        max_length=255,
        verbose_name=_(u'Text'),
        help_text=_(u'This text will be shown as-is in the schedule'),
    )

    def __unicode__(self):
        return u'{text} ({programme})'.format(text=self.text, programme=self.programme)

    class Meta:
        verbose_name = _(u'freeform organizer')
        verbose_name_plural = _(u'freeform organizers')