# IMPORTANT NOTE: DiscordID fetch from RobloxID has not been implemented into the program as of yet. 
# ANOTHER IMPORTANT NOTE: Sometimes people may link an alternate Roblox account to their Discord account. We can't do much about that.

import requests as http

# Variables
bloxlinkApi = "https://api.blox.link/v1/user" # Bloxlink API
erynApi = "https://verify.eryn.io/api/roblox" # Eryn API (for RTD)
robloxUserList = []
discordUserList = []

# Roblox user fetch
def fetchRobloxId(id):
  # Fetch the API and store the response inside inf
  inf = http.get(bloxlinkApi + "/{}".format(int(id)))
  if inf.status_code == 200: # If the request was successful:
    # Convert request into a JSON, get the roblox account id,
    # and return
    fid = inf.json()
    if fid["status"] == "ok":
      return fid["primaryAccount"]
    else:
      print("Error: {}".format(fid["error"]))
  else:
    print("Error {}: The fetch pooed itself.".format(inf.status_code))
    
# Discord user fetch
def fetchDiscordId(id):
  disc = http.get(erynApi + "/{}".format(int(id)))
  if disc.status_code == 200:
    did = disc.json()
    if did["status"] == "ok":
      return did["users"]
    else:
      print("Error: {}".format(did["error"]))
  else:
    print("Error {}: Something went wrong.".format(disc.status_code))

    
# User input processing
def theFunny():
  userinput = input("> ").split()
# An input of "q" will quit the theFunny function.
  if userinput[0] == "q":
    return None
# User inputs a valid DiscordID connected to the Bloxlink API to return a RobloxID
  elif userinput[0] == "dtr":
    try:
      robloxId = fetchRobloxId(userinput[1])
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
  elif userinput[0] == "rtd":
    try:
      discordId = fetchDiscordId(userinput[1])
      for id in discordId:
        print(id)
        discordUserList.append(id)
      print("If you wish to lookup the Discord tag associated with this Discord ID, go to this website: " + " https://discord.id/")
    except:
      print("Valid Roblox ID not entered. Please try again.")
# funny
  else:
    print('foo')

  return theFunny()
# Start the program loop
theFunny()