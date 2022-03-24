import requests as http

# Variables
api = "https://api.blox.link/v1/user" # Bloxlink API
robloxUserList = []

#roblox user fetch
def fetchId(id):
  # Fetch the API and store the response inside inf
  inf = http.get(api + "/{}".format(int(id)))

  if inf.status_code == 200: # If the request was successful:
    # Convert request into a JSON, get the roblox account id,
    # and return
    fid = inf.json()["primaryAccount"]
    return fid

# User input processing
def theFunny():
  userinput = input("> ").split()
# An input of "q" will quit the theFunny function.
  if userinput[0] == "q":
    return None
# User inputs a valid DiscordID connected to the Bloxlink API to return a RobloxID
  elif userinput[0] == "dtr":
    try:
      robloxId = fetchId(userinput[1])
      print("Roblox ID: " + robloxId)
      print("Roblox Profile: " + " https://www.roblox.com/users/" + robloxId + "/profile")
      
      robloxUserList.append(robloxId)
# If input is not a valid DiscordID or DiscordID is not connected to the BloxlinkAPI, return an error message and restart loop.
    except Exception:
      print("Valid DiscordID not entered. Please try again.")
  elif userinput[0] == "listusers":
    print("Current roblox IDs: ")
    for id in robloxUserList:
      print(id)   
# funny
  else:
    print('foo')
  return theFunny()

# Start the program loop
theFunny()