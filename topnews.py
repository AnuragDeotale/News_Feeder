import requests  # Used to make an HTTP request to fetch the RSS feed
import xml.etree.ElementTree as ET # Used to parse the XML format of the RSS feed

RSS_FEED_URL = "http://feeds.bbci.co.uk/news/rss.xml" # This is the BBC News RSS feed URL that provides news in XML format


def loadRSS():
    '''Utility function to load RSS feed'''
    resp = requests.get(RSS_FEED_URL)  # Fetch data from the URL
    return resp.content                # Return the raw XML content
 
def parseXML(rss):
    '''Utility function to parse XML format RSS feed'''
    root = ET.fromstring(rss)  # Convert XML string into an Element Tree Object
    newsitems = []             # List to store extracted news items
    for item in root.findall('./channel/item'):  # Find all <item> tags in the RSS feed
        news = {} Dictionary to Store news details
        for child in item:
            if child.tag == '{http://search.yahoo.com/mrss/}content': # If the tag is a media content
                news['media'] = child.attrib['url']                   # Extract image/video url
            else:
                news[child.tag] = child.text         # Store text content (title, link, description, etc.)
        newsitems.append(news)                        # Append to list
    return newsitems                                  # Return the list of news items

def topStories():
    '''Main function to generate and return news items'''
    rss = loadRSS()  # Load the RSS feed
    newsitems = parseXML(rss) # Parse the XML content
    return newsitems          # Return the list of news articles
