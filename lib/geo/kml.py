#http://pyparsing.wikispaces.com/HowToUsePyparsing
from pyparsing import Word, alphas, alphanums, nums, Literal, restOfLine, OneOrMore, \
    empty, Suppress, replaceWith, Group, Optional
from pyparsing import makeHTMLTags, withAttribute, SkipTo
from pyparsing import Suppress

#Dirty, dirty hack. Move to proper XML soonest

#td_start, td_end = makeHTMLTags("td")
pm_start, pm_end = makeHTMLTags("Placemark")
name_start, name_end = makeHTMLTags("name")
desc_start, desc_end = makeHTMLTags("description")
poly_start, poly_end = makeHTMLTags("Polygon")
ed_start, ed_end = makeHTMLTags("ExtendedData")


placemark_set = ( pm_start 
               #+ SkipTo(name_start) + name_start + SkipTo(name_end)("name") + name_end #Note: this might be a CDATA Section
               + Optional(SkipTo(desc_start) + desc_start + SkipTo(desc_end)("description") + desc_end)
               #+ SkipTo(desc_start) + desc_start + "<![CDATA[" + SkipTo("]]>")("description") + ']]>' + desc_end
               + SkipTo(poly_start) + poly_start + SkipTo(poly_end)("polygon") + poly_end
               + Optional(SkipTo(ed_start) + Group(SkipTo(ed_end) + ed_end)("ext_data"))
               + SkipTo(pm_end) + pm_end
             )


def gen_record(text):
    for data, startloc, endloc in placemark_set.scanString(text):
        yield data

    #print data.pid[1], ': ' , data.coords.split()[0].rsplit(',', 1)[0]
    #lat, lng = border.split('|')[0].split(',')
    #qstr = urllib.urlencode({'formatted' : 'true', 'lat': lat, 'lng' : lng, 'username': 'zepheira'})
    #resp = urllib2.urlopen(BASE_LAT_TO_ZIP + qstr)
    #resp_data = json.load(resp)
    #zipcode = resp_data["postalCodes"][0]["postalCode"]


#-----------------------------------

import re
#Now we have 2 problems ;)
#Dirty, dirty hack. Move to proper XML soonest

PM_PID_PAT = re.compile(r'<Placemark.*?(<description>.*?<td>(PIN|PARCELID)</td>\s*<td>(.*?)</td>.*?</description>.*?)?<Polygon>.*?<coordinates>(.*?)</coordinates>.*?</Polygon>.*?</Placemark>', flags=re.DOTALL)

def gen_record(text):
    for m in PM_PID_PAT.finditer(text):
        yield (m.group(3), m.group(4))


def fix_point_array(coord_array):
    #KML seems to use lng, lat arrays, and Exhibit uses lat/long
    points = []
    for p in coord_array.split():
        coords = p.split(',')
        lng, lat = coords[0], coords[1]
        points.append(','.join((lat, lng)))
    #border = '|'.join(points)
    return points


