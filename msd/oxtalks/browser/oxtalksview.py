from DateTime import *
from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from msd.oxtalks import oxtalksMessageFactory as _

# from urllib2 import *
import requests
# import json

class IoxtalksView(Interface):
    """
    oxtalks view interface
    """

    def test():
        """ test method"""


class oxtalksView(BrowserView):
    """
    oxtalks browser view
    """
    implements(IoxtalksView)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        
    @property
    def title(self):
         return self.context.Title

        
    def getResults(self):
        
        listID = self.context['listID']
        
        request_string = 'http://talks.ox.ac.uk/show/json/%s' %(listID)
        
        conn = requests.get(request_string)
        rsp = conn.json()
        
        return rsp

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def currententries(self):
        """
        test method
        """
        
        results_set = self.getResults()
        allItems = []
        
        for x in results_set:
            description = x.get('abstract_filtered','')
            Title = x.get('title')
            if x.get('venue'):
                place_array = x.get('venue','')
                venue = place_array.get('name','')
            else:
                venue = ""
            if x.get('series'):
                series_array = x.get('series','')
                series = place_array.get('name','')
            else:
                series = ""
            talk_id = x.get('id','')
            series_id = x.get('series_id')
            speaker = x.get('name_of_speaker','')
            start_time = x.get('start_time','')
            end_time = x.get('end_time','')
            special_message = x.get('special_message','')
            fm_startdate = DateTime(start_time).strftime('%A, %d %B, %Y').replace(', 0',', ')
            fm_starttime = DateTime(start_time).strftime('%I.%M %p').strip('0')
            fm_endtime = DateTime(end_time).strftime('%I.%M %p').strip('0')
            link = "http://talks.ox.ac.uk/talk/index/%s" %(talk_id)
            ical = "http://talks.ox.ac.uk/talk/vcal/%s" %(talk_id)

            allItems.append({'description': description,
                'Title': Title,
                'speaker': speaker,
                'venue': venue,
                'series': series,
                'series_id': series_id,
                'talk_id': talk_id,
                'ical': ical,
                'link': link,
                'start_time': start_time,
                'end_time': end_time,
                'special_message': special_message,
                'fm_startdate': fm_startdate,
                'fm_starttime': fm_starttime,
                'fm_endtime': fm_endtime,})
                
                            
                            
        allItems.sort(key=lambda x: x["start_time"], reverse=False)
                
        return allItems
