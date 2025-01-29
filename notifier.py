import time
from plyer import notification # Import notification module from plyer
from topnews import topStories # Import function to fetch news from RSS feed

try:
    # Fetch news items from the RSS feed
    newsitems = topStories()
    
    # Check if any news items were fetched
    if not newsitems:
        print("No news items found. Please check the RSS feed.")
    else:
         # Iterate through the news items one by one
        for newsitem in newsitems:
            # Display a desktop notification
            notification.notify(
                title=newsitem['title'], # News headline as title
                message=newsitem['description'], # News description as message
                timeout=10,  # Notification duration in seconds
            )

            # Short delay between notifications
            time.sleep(15)

# Handle any errors that occur during exception
except Exception as e:
    print("An error occurred:", str(e))
