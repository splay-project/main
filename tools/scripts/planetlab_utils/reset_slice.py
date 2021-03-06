#!/usr/bin/env python

import xmlrpclib
import sys
import urllib

if len(sys.argv) != 4:
	print "Remove all nodes from the specified slice"
	print "Usage: ./reset_slice.py pl_username pl_pwd pl_slice_name"
	sys.exit(2)

api_server = xmlrpclib.ServerProxy('https://www.planet-lab.eu/PLCAPI/')
auth = {}
auth['Username'] = sys.argv[1] # <-- substitute your actual username here
auth['AuthString'] = sys.argv[2] # <-- substitute your actual password here
auth['AuthMethod'] = "password"

slice_name=sys.argv[3]

# the slice's node ids
node_ids = api_server.GetSlices(auth,slice_name,['node_ids'])[0]['node_ids']
api_server.DeleteSliceFromNodes(auth, sys.argv[3], node_ids)
