from django.http import JsonResponse
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit

asset = {
        'data': {
            'clientes': [{
              'firstname': 'Gibran',
              'lastname': 'Otazo',
              'birthdate': '1986-07-15',
              'curp': 'OASG860715HNETNB08',
              'id': '735f75110cb42a2a86d33cb1f574c930265825ed882d50cd00a339baee246964',
            },
            {
              'firstname': 'Gerardo',
              'lastname': 'Linares',
              'birthdate': '1986-07-15',
              'curp': 'IAGG870415DVHJ08',
              'id': '735f75110cb42a2a86d33cb1f574c930265825ed882d50cd00a339baee246964',
            }],
        },
}



# Create your views here.
def foo(request):

    firstname=request.GET['firstname']
    lastname=request.GET['lastname']
    birthdate=request.GET['birthdate']
    curp=request.GET['curp']
    sector=request.GET['sector']

    for i in list(range(len(asset['data']['clientes']))):
        if asset['data']['clientes'][i]['firstname'] == firstname and asset['data']['clientes'][i]['lastname'] == lastname and asset['data']['clientes'][i]['birthdate'] == birthdate and asset['data']['clientes'][i]['curp'] == curp:
            idtx = asset['data']['clientes'][i]['id']
            break

    bdb = BigchainDB()

    creation_tx = bdb.transactions.retrieve(idtx)
    response = creation_tx['asset']

    return JsonResponse(response)
