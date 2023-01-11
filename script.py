import requests as req

#Print the version of requests (virtualenv)
print("Version of \"requests\" is: " + req.__version__)

#Get the google homepage
response = req.get("https://www.google.com")
print("Got code " + str(response.status_code))