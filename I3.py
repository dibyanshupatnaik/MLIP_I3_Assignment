import pandas as pd
from ydata_profiling import ProfileReport

# Read the CSV file
df = pd.read_csv('rating_550mb_snapshot.csv', names=[
    'time', 'userid', 'movieid', 'rating'], header=None)

# Generate a profile report
profile = ProfileReport(df, title='Profile Report', explorative=True)

# Save the report to an HTML file
profile.to_file("profile_report.html")
