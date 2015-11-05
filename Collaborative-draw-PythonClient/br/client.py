from suds.client import Client
from time import sleep
namespace = "http://quadro.ws/"  
wsdl = "http://10.0.200.116:54321/quadro?wsdl"  
client = Client(wsdl)
print client
result = client.service.getDesenho()
print result

for x in xrange (10,100)  : 
    #sleep (0.5)
    client.service.setRemetente("MAM")
    client.service.setDesenho("<circle id=\"100\" cx=\"%d\" cy=\"100\" r=\"100\" stroke=\"#FF0000\" stroke-width=\"10\" fill=\"#0000FF\" />" %x )
    print client.service.getDesenho()
    print client.service.getRemetente()
#for x in range(0, 3):
#   print "We're on time %d" % (x)