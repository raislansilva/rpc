import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("tipo: %s" % str(proxy.is_type(True)))
   
