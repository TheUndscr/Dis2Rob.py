# IMPORTANT NOTE: DiscordID fetch from RobloxID has not been implemented into the program as of yet. 
# ANOTHER IMPORTANT NOTE: Sometimes people may link an alternate Roblox account to their Discord account. We can't do much about that.
import sys
sys.path.insert(1, "mainmods")
#color for something idk
Red = "\033[0;31m"
# imports
import time
import fetcher
ft = fetcher.Fetcher()
#info
print("Dis2Rob\n\ndtr {discord id}: finds the discord user\'s roblox account.\nlist: Show all Discord ID\'s and their respective Roblox username\'s and usernames.\nrtd {roblox id}: never coming")

# User input processing
def theFunny():
  userinput = input("> ").split()
# An input of "q" will quit the theFunny function.
  if userinput[0] == "q":
    return None
# User inputs a valid DiscordID connected to the Bloxlink API to return a RobloxID
  elif userinput[0] == "dtr":
    try:
      robloxId = ft.fetchRobloxId(userinput[1])
      print("Roblox ID: " + robloxId)
      print("Roblox Profile: " + " https://www.roblox.com/users/" + robloxId + "/profile")
      #print("Roblox Username: " + username)
# If input is not a valid DiscordID or DiscordID is not connected to the BloxlinkAPI, return an error message and restart loop.
    except Exception:
      print("Valid DiscordID not entered. Please try again.")
  elif userinput[0] == "list":
    ft.listUsers("r")
  elif userinput[0] == "rtd":
    print("This program will spontaneously combust in 10 seconds.")
    for i in range(10, 0, -1):
      print(str(i) + "...")
      time.sleep(1)
    print(Red + "Gogbey.")  
    exit()
# funny
  else:
    print('foo')

  return theFunny()
# Start the program loop
theFunny()