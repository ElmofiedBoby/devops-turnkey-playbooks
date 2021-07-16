from caprover_api import caprover_api
import sys
#Argument syntax: git-installer.py,app_name,url

cap = caprover_api.CaproverAPI(
    dashboard_url=sys.argv[2],
    password="captain42"
)

cap.delete_app(app_name=sys.argv[1])
