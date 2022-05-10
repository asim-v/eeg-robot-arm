"""Small example Emotiv OSC
This program listens to several addresses, and prints some information about
received packets.
"""

import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server

PORT_NUMBER = 8080
IP_DEFAULT = "127.0.0.1"

def filter_handler(address,*args):
  print(f"{address}: {args}")

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default=IP_DEFAULT, help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=PORT_NUMBER, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()


  #=== Mental Commands
  dispatcher.map("/com/neutral", filter_handler)
  dispatcher.map("/com/left", filter_handler)
  dispatcher.map("/com/right", filter_handler)
  dispatcher.map("/com/lift", filter_handler)



  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()