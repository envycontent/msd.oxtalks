"""Definition of the Oxford Talks List content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from msd.oxtalks import oxtalksMessageFactory as _

from msd.oxtalks.interfaces import IOxfordTalksList
from msd.oxtalks.config import PROJECTNAME

OxfordTalksListSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'listID',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"List ID"),
            description=_(u"Enter the ID of the list, you can usually find this by looking at the web address of the list."),
        ),
        required=True,
        default=_(u"4427"),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

OxfordTalksListSchema['title'].storage = atapi.AnnotationStorage()
OxfordTalksListSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(OxfordTalksListSchema, moveDiscussion=False)


class OxfordTalksList(base.ATCTContent):
    """An Oxford Talks Events or Seminar List"""
    implements(IOxfordTalksList)

    meta_type = "OxfordTalksList"
    schema = OxfordTalksListSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    listID = atapi.ATFieldProperty('listID')


atapi.registerType(OxfordTalksList, PROJECTNAME)
