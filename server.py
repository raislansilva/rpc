from xmlrpc.server import SimpleXMLRPCServer

def is_type(n):
    print("Requisição recebida com o seguinte argumento: " + str(n))
    return str(type(n)) 

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(is_type, "is_type")
server.serve_forever()
