from webapp import app
import datetime, time

@app.template_filter("formater_date")

def formater_date(text):
    if isinstance(text, (datetime.date, datetime.datetime)):
        return time.strftime("%d / %m /%y")
    return text
