# Class for fetching APIs
import requests
class Fetcher:
  def __init__(self):
    # Apis
    self.bloxlinkApi = "https://api.blox.link/v1/user"
    self.robloxApi = "https://api.roblox.com/"
    
    self.placeholder = ""
    
    # User lists
    self.robloxUserList = {}
    self.discordUserList = {}

    # Libs
    self.http = requests
  def listUsers(self, ltype):
    if ltype == "r":
      print("Current Roblox Id\'s: ")
      for i in self.robloxUserList:
        print("DiscordID: {}\nRoblox user: {}\n\n".format(str(i), self.robloxUserList[i]))

      print("{} current id\'s".format(len(list(self.robloxUserList))))
  def fetchRobloxId(self, id):
    # Fetch the API and store the response inside inf
    inf = self.http.get(self.bloxlinkApi + "/{}".format(int(id)))
    if inf.status_code == 200: # Success
      # Convert response to JSON
      fid = inf.json()
      if fid["status"] == "ok":
        username = self.http.get(self.robloxApi + "{}".format("users/" + str(fid["primaryAccount"]))).json()
        # Pair the Roblox ID with its Username
        self.robloxUserList[str(id)] = username["Username"]
        # Return the id
        return fid["primaryAccount"]
      else:
        print("Error: {}".format(fid["error"]))
    else:
      print("Error {}: The fetch pooed itself.".format(inf.status_code))

  '''def fetchDiscordId(self, id):
   #  Fetch the API and store
    disc = self.http.get(self.placeholder + "/{}".format(int(id)))
    
    if disc.status_code == 200:  Success
       Convert response to JSON
      did = disc.json()
    
      if did["status"] == "ok":
         Return a list of users
        return did["users"]
      else:
        print("Error: {}".format(did["error"]))
    else:
      print("Error {}: Something went wrong. Your computer will blow up in mere seconds.".format(disc.status_code))'''

# roblox - discord user grouping

 