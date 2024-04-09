from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from libs.Underscore import U

class ConfigByRCUType(APIView):
    def post(self, request):
        lstRCUList = request.data.get('lstRCUList', [])
        lstgroup = U.groupBy(lstRCUList, "RoomType_id")
        
        lstRCuByRCUType = U.map(lstgroup.values(), lambda group: {'RCUTypeId': group[0]['RoomType_id'], 'data': group})
        
        return Response({"success": True, "message": "Record Found...", "data": [{"api":"is working"}]})
        
    