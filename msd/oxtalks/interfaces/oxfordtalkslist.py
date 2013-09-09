from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from msd.oxtalks import oxtalksMessageFactory as _



class IOxfordTalksList(Interface):
    """An Oxford Talks Events or Seminar List"""

    # -*- schema definition goes here -*-
    listID = schema.TextLine(
        title=_(u"List ID"),
        required=True,
        description=_(u"Enter the ID of the list, you can usually find this by looking at the web address of the list."),
    )
#
