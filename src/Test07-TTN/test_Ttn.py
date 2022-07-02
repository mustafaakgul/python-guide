
import time
import ttn

app_id = "kontrolmatik_app_lora"
access_key = "ttn-account-v2.y0XaLuVSSWbgM3aVvlIZPfi6HwEipEyMMiHT5nAqmtI"

def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  print("message", msg.payload_fields.text)


while(1):
    handler = ttn.HandlerClient(app_id, access_key)

    # using mqtt client
    mqtt_client = handler.data()
    mqtt_client.set_uplink_callback(uplink_callback)
    mqtt_client.connect()
    time.sleep(10)
    mqtt_client.close()

    # using application manager client
    app_client =  handler.application()
    my_app = app_client.get()
    #print("app", my_app)
    my_devices = app_client.devices()
    #print("devices", my_devices)