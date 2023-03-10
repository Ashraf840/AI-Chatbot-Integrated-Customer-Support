from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import sync_to_async, async_to_sync
import json
from home.models import CustomerSupportRequest
from channels.layers import get_channel_layer
from ..cso_connectivity_models import CSOOnline, CSOConnectedChannels


def create_channel_conn(room_slug, channel_name, cso_email):
    print('*'*10, "create_channel_conn() func is called")
    print("room slug:", room_slug)
    channel_name = channel_name.replace('specific.', '')  # remove the prefix from each channel-name before storing into the db
    print("channel name:", channel_name)
    print("cso email:", cso_email)
    print('create channel-record of cso-user using email in the "CSOConnectedChannels" model.')
    CSOConnectedChannels.objects.create(
        cso_email=cso_email,
        room_slug=room_slug,
        channel_value=channel_name
    )

def remove_channel_conn(room_slug, channel_name, cso_email):
    print('*'*10, "remove_channel_conn() func is called")
    print("room slug:", room_slug)
    channel_name = channel_name.replace('specific.', '')  # remove the prefix from each channel-name before storing into the db
    print("channel name:", channel_name)
    print("cso email:", cso_email)
    print('[first check if exist] remove channel-record of cso from the "CSOConnectedChannels" model.')
    try:
        CSOConnectedChannels.objects.get(
            cso_email=cso_email,
            room_slug=room_slug,
            channel_value=channel_name
        ).delete()
    except CSOConnectedChannels.DoesNotExist:
        print('No such active channel exists!')

# Can make a common function (used in "home/consumers/cso_visitor_chat_consumer.py")
def make_user_online(user):
    # Check if the user's active; otherwise change it to True
    if not user.is_active:
        user.is_active = True
        user.save()

def make_user_offline(user):
    # Check if the user's active; then change it to False
    if user.is_active:
        user.is_active = False
        user.save()

def active_user_online(room_slug, channel_name, cso_email):
    """
    This func is responsible for creating new record in the "CSOOnline" model if no record found of the CSO based on certain condition.
    """
    print('*'*10, "active_user_online() func is called")
    print("cso email:", cso_email)
    print("room slug:", room_slug)
    print("channel name:", channel_name)

    try:
        # Check if the CSO is already online in the system
        cso_online_obj = CSOOnline.objects.get(cso_email=cso_email, room_slug=room_slug)
        print('Found active cso record!', cso_online_obj)
        # Make the CSO online if s/he is not online by passing the "cso_online_obj" entirely
        make_user_online(cso_online_obj)
        # Create multiple channels of the same CSO to track that cso's-online-status regardless of creating duplicate multiple tabs.
        create_channel_conn(room_slug=room_slug, channel_name=channel_name, cso_email=cso_email)
    except CSOOnline.DoesNotExist:
        # Create CSO online record
        cso_online_obj = CSOOnline.objects.create(cso_email=cso_email, room_slug=room_slug)
        print('Created a active cso record!', cso_online_obj)
        create_channel_conn(room_slug=room_slug, channel_name=channel_name, cso_email=cso_email)

def count_active_channel(room_slug, cso_email):
    # filter-search using cso-email and room-slug
    print('*'*10, "count_active_channel() func is called")
    return CSOConnectedChannels.objects.filter(
        cso_email=cso_email,
        room_slug=room_slug
    )

def deactive_user_online(room_slug, channel_name, cso_email):
    """
    This func is responsible for deactivating the old user in the "CSOOnline" model based on certain condition.
    """
    print('*'*10, "deactive_user_online() func is called")
    print("room slug:", room_slug)
    print("cso email:", cso_email)
    print('check cso online record using email in the "CSOOnline" model.')
    try:
        cso_online_obj = CSOOnline.objects.get(cso_email=cso_email, room_slug=room_slug)
        print('Intially make the cso offline!', cso_online_obj)
        
        # Remove the exisiting active channel(s) of the same CSO for each "Screen-refresh"/"Duplicate-tab-creation" of the smae page
        remove_channel_conn(room_slug=room_slug, channel_name=channel_name, cso_email=cso_email)
        total_active_channel = count_active_channel(room_slug=room_slug, cso_email=cso_email)
        print('total_active_channel (cso):', total_active_channel)
        # [INITIAL-STEP, later firstly check if the total opened channel(s) of that individual CSO is 0 before making the CSO's status offline] 
        if len(total_active_channel) == 0:
            # Make the user offline if it's online by passing the "user_online_obj" entirely, so that the follwing func doesn't require to query the "ChatSupportUserOnline" model before making the user offline.
            make_user_offline(cso_online_obj)
    except CSOOnline.DoesNotExist:
        print('CSO doesn\'t exist to make the CSO offline!')


# Customer Support Dashboard Consumer
class SupportDashboardConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super(SupportDashboardConsumer, self).__init__(*args, **kwargs)
        self.room_name = None
        self.room_name_normalized = None
        self.room_group_name = None
        self.user_obj = None
    
    # [Default method] Create an asynchronous connection-function
    def connect(self):
        print("#"*50)
        print("[connect() method] Connected to backend consumer class: SupportDashboardConsumer")
        # self.room_name = 'dashboard'
        # self.room_group_name = 'chat_%s' % self.room_name
        self.room_name = self.scope['url_route']['kwargs']['cso_mail']
        print(f"room name: {self.room_name}")
        self.room_name_normalized="".join(ch for ch in self.room_name if ch.isalnum())   # keeps only alphanumeric-chars in the room-name. [Ref]: https://www.scaler.com/topics/remove-special-characters-from-string-python/
        self.room_group_name = 'chat_dashboard_%s' % self.room_name_normalized    # THIS pattern is required to sent any asynchrobous msg to this consumer-channel
        print(f"room-group name: {self.room_group_name}")
        self.user_obj = self.scope['user']
        # print(f"Newly Connected (username): {self.user_obj.username}")
        print(f'Channel name: {self.channel_name}')

        async_to_sync(active_user_online(cso_email=self.user_obj.email, room_slug=self.room_name_normalized, channel_name=self.channel_name))

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name  # channels automatically fixes room-name?
        )
        async_to_sync(self.accept())

        # get all the customer-support-requests using the staticmethod of "CustomerSupportRequest" model
        all_support_reqs = CustomerSupportRequest.get_customer_support_reqs()
        print(f"All support reqs: {all_support_reqs}")

        # what is get_channel_layer?????
        channel_layer_var = get_channel_layer()
        print(f"channel_layer_var: {channel_layer_var}")

        # Send to the single specific CSO to his/her dashboard websocket; who connects to this consumer currently
        self.send(text_data=json.dumps({
            'status': 'Backend Consumer (Websocket): Connected - initial hit from frontend - then conn payload sent from backend',
            'payload': 'Any kind of python object payload is sent to frontend WebSocket onmessage() method',
            'payload2': f'{all_support_reqs}',
        }))
        print("#"*50)

    # Default method of "WebsocketConsumer" class
    # Receive the msg from frontend & broadcast it to the entire channel
    def receive(self, text_data=None, bytes_data=None):
        print("#"*50)
        print("[recieve() method] Recieved data to backend consumer class: SupportDashboardConsumer")
        print("#"*50)
    
    # Custom method: send all new support-req from the db-signal's (home.signals.customer_support_request_signal) channel-group-send method.
    def new_support_req(self, event):
        new_supprt_reqst = event['new_support_request']
        self.send(text_data=json.dumps({
            'new_supprt_reqst': new_supprt_reqst,
        }))

    # Default method of "WebsocketConsumer" class
    def disconnect(self, *args, **kwargs):
        print("#"*50)
        # call the deactive_user_online() func
        async_to_sync(deactive_user_online(cso_email=self.user_obj.email, room_slug=self.room_name_normalized, channel_name=self.channel_name))
        
        async_to_sync (self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        print("[disconnect() method] Disconnected from backend consumer class: SupportDashboardConsumer")
        print("#"*50)
