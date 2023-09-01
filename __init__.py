from quick_resto_API.quick_resto_api import QuickRestoApi
from quick_resto_API.operations_with_objects.list_request.filter import Filter

apiClass = QuickRestoApi(login="zg886", password="hgRfgJb3", use_https=True)
parameters = {
"moduleName":"front.orders"
}
class_name="ru.edgex.quickresto.modules.front.orders.OrderInfo"
filterOfOrder = Filter(field="regTime", operation="range", value={"since":"1688169600", "till":" 1690675200"})
module_name = "front.orders"
getApiClass = apiClass.get("api/list", parameters= parameters)
print(getApiClass)










