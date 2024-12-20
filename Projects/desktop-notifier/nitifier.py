from notifypy import Notify
import news

notification = Notify()

news = news.main()

for item in enumerate(news[:1]):
    notification.title = item[1]["title"]
    notification.message = item[1]["link"]
    notification.description = item[1]["description"]

try:
    notification.send()
except Exception as e:
    print(f"Error sending notification: {e}")
