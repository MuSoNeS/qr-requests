from quick_resto_API import quick_resto_api
from quick_resto_API.quick_resto_api import QuickRestoApi
from quick_resto_API.quick_resto_objects.quick_resto_object import QuickRestoObject
from quick_resto_API.quick_resto_objects.modules.front.order_info import OrderInfo
from quick_resto_API.operations_with_objects.list_request.list_request import ListRequest

apiClass = QuickRestoApi(login="zg886", password="hgRfgJb3", use_https=True)
apiClass.__init__(login="zg886", password="hgRfgJb3", use_https=True)


baseUrl = apiClass.base_url
parameters = {
"moduleName":"front.orders",
"objectId": 0
}
getApiClass = apiClass.get("api/list", parameters= parameters)
print(getApiClass.json())
#class_name="front.orders",id=5




