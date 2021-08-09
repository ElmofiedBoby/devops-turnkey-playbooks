from caprover_api.caprover_api import caprover_api
import importlib
import sys

importlib.reload(caprover_api)
#Argument syntax: git-installer.py,app_name,url

print(sys.argv[1])
print(sys.argv[2])

cap = caprover_api.CaproverAPI(
    dashboard_url=sys.argv[2],
    password="captain42"
)

cap.deploy_app(
    app_name=sys.argv[1],
    image_name="tomcat:latest"
)

cap.update_app(
    app_name=sys.argv[1],
    port_mapping="8888:8080"
)
