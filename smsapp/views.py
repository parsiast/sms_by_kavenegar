from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from smsapp.models import Smstosend
from smsapp.serializers import Tosend 
from kavenegar import *

@api_view(['GET','POST'])
def sms(request):
    if request.method == 'GET' :
        allsms=Smstosend.objects.all()
        serializer=Tosend(allsms,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=Tosend(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def sms_send(self, params=None):
    return self._request('sms', 'send', params)


@api_view(['GET','POST'])
def smssender(request,user_id):
    try:
        sms_to_send = Smstosend.objects.get(id=user_id)
        api = KavenegarAPI(sms_to_send.apikey)
        params = {
            'receptor': sms_to_send.receptor,  # The recipient's phone number
            'message': sms_to_send.message,    # The message to send
        }
        response = api.sms_send(params)
        return Response(response, status=status.HTTP_200_OK)
    except Smstosend.DoesNotExist:
        return Response({'error': 'SMS entry not found'}, status=status.HTTP_404_NOT_FOUND)
    except APIException as e:
        
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)




        
    

    


