from twilio import twiml
from twilio.rest import TwilioRestClient
import phonenumbers
from models import neighbor

account = "AC924df7b4368631de1e0ce404a32292c5"
token = "4298bb286885ec24d7ce80c69948c93b"
neighborlyphone = '+17024302790'

def broadcastfavor(request)
    user_id = request.POST.get('user_id')
    item = request.POST.get('item')

    userzip = user.zip_code
    neighbors = User.objects.get(zip_code=userzip)

    for neighbor in neighbors:
        sendmessage(user,neighbor)

def sendmessage(borrower, lender):
    client = TwilioRestClient(account, token)
    msg = borrower.name + " needs a " + borrower.item + ". Can you help him out? His number is " + borrower.phone
    message = client.sms.messages.create(to=lender.phone, from_=neighborlyphone,
                                         body=msg)
    return message

urlpatterns = patterns('twiliostuff',
    url(r'^broadcastfavor$', broadcastfavor),
)
