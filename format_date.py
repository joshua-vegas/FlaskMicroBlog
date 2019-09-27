import datetime, time
from webapp import create_app

app = create_app()

@app.template_filter("formater_date")

def formater_date(text):
    if isinstance(text, (datetime.date, datetime.datetime)):
        return time.strftime("%d / %m /%y")
    return text
