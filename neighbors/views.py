from django.http import HttpResponse
from django.shortcuts import render_to_response
from neighbors.models import User, Request
from twilio import twiml
from twilio.rest import TwilioRestClient

def broadcast(request):
    info = {'fname': request.POST.filter('fname'),
                'lname': request.POST.filter('lname'),
                'zipcode': request.POST.filter('zipcode'),
                'phone': request.POST.filter('phone'),
                'item': request.POST.filter('item')}
    for neighbor in User.objects.get(zip_code=zipcode):
        sendmessage(neighbor, info)

    return render_to_response('broadcastsent.html', info)


def sendmessage(neighbor, info):
    account = "AC924df7b4368631de1e0ce404a32292c5"
    token = "4298bb286885ec24d7ce80c69948c93b"
    neighborlyphone = '+17024302790'

    client = TwilioRestClient(account, token)
    msg = info.fname + " " + info.lname + " needs a " + info.item + ". Help 'em out! His number is " + info.phone
    message = client.sms.messages.create(to=neighbor.phone_number, from_=neighborlyphone, body=msg)
