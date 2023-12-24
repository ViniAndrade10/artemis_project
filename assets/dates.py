from datetime import datetime, timedelta

today_date = datetime.now()
start_date = today_date - timedelta(365.25 * 2)

start_date = start_date.strftime("%Y-%m-%d")
end_date = datetime.today().strftime("%Y-%m-%d")