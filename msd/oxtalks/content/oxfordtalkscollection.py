"""Definition of the Oxford Talks Collection
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from msd.oxtalks import oxtalksMessageFactory as _

from msd.oxtalks.interfaces import IOxfordTalksCollection
from msd.oxtalks.config import PROJECTNAME

OxfordTalksCollectionSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.LinesField(
        'feeds',
        storage=atapi.AnnotationStorage(),
        widget=atapi.LinesWidget(
            label=_(u"Feeds"),
            description=_(u"Enter the URLs of the feeds you want to use"),
        ),
        required=True,
        default= ["http://talks.ox.ac.uk/api/talks/search?from=today&organising_department=oxpoints:23232740",],
    ),
    
    atapi.StringField(
        'limitNum',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Limit"),
            description=_(u"Enter the number of items to show"),
        ),
        required=True,
        default=_(u"10"),
    ),
    
    atapi.StringField(
        'styleSheet',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Stylesheet"),
            description=_(u"Enter the name of your stylesheet"),
        ),
        required=True,
        default=_(u"teal"),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

OxfordTalksCollectionSchema['title'].storage = atapi.AnnotationStorage()
OxfordTalksCollectionSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(OxfordTalksCollectionSchema, moveDiscussion=False)


class OxfordTalksCollection(base.ATCTContent):
    """An Oxford Talks Collection of Feeds"""
    implements(IOxfordTalksCollection)

    meta_type = "OxfordTalksCollection"
    schema = OxfordTalksCollectionSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    feeds = atapi.ATFieldProperty('feeds')
    limitNum = atapi.ATFieldProperty('limitNum')
    styleSheet = atapi.ATFieldProperty('styleSheet')
    


atapi.registerType(OxfordTalksCollection, PROJECTNAME)
