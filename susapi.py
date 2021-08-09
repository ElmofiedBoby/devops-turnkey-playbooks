from caprover_api.caprover_api import caprover_api
import sys

# arguments syntax: susapi.py NAME PERSISTENT(T/F) URL

cap = caprover_api.CaproverAPI(
    dashboard_url=sys.argv[3],
    password="captain42"
)

if sys.argv[2] == "True" or sys.argv[2] == "true" or sys.argv[2] == "t" or sys.argv[2] == "T":
    based = True
else:
    based = False

cap.create_and_update_app(
    app_name=sys.argv[1],
    has_persistent_data=based
)
