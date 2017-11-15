import json
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.nasa.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.nasa.gov,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("y77d-th95", limit=45716)

with open('data.json', 'w') as f:
     json.dump(results, f)