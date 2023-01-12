import requests as req

#Print the version of requests (virtualenv)
print("Version of \"requests\" is: " + req.__version__)

#Get the google homepage
response = req.get("https://www.google.com")
print(response.status_code)

#Print own source code from github
ghResponse = req.get("https://raw.githubusercontent.com/jd-lo/CMPUT-404-Lab-1/main/script.py")
print(ghResponse.content)