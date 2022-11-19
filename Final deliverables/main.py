import paho.mqtt.client as mqtt
import time
import random
import json


def run():
    ORG = "nnj60r"
    DEVICE_TYPE = "IBM"
    DEVICE_ID = "IBM-2"
    TOKEN = "vA91c?4n?3WeS-2qnf"

    server = ORG + ".messaging.internetofthings.ibmcloud.com"
    pubTopic1 = "iot-2/evt/temp/fmt/json"
    pubTopic2 = "iot-2/evt/pH/fmt/json"
    pubTopic3 = "iot-2/evt/turb/fmt/json"
    # pubTopic3="iot-2/evt/wf/fmt/json";
    token = TOKEN
    authMethod = "use-token-auth"
    clientId = "d:" + ORG + " : " + DEVICE_TYPE + " : " + DEVICE_ID
    mqttc = mqtt.Client(client_id=clientId)
    mqttc.username_pw_set(authMethod, token)
    mqttc.connect(server, 1883, 60)

    while True:
        try:
            # Print the values to the serial port
            temperature_c = random.randint(30, 40)*1.0
            temperature_f = temperature_c * (9/5) + 32.0
            pH = random.randint(0, 14) * 1.0
            turb = random.uniform(1, 2)
            print("Temp: {:.2f} F / {} C pH: {} Turbidity:{:.2f}NTU".format(
                temperature_f, temperature_c, pH, turb))
            payload = {"temp": temperature_c, "pH": pH, "turb": round(turb, 2)}
            mqttc.publish(pubTopic1, json.dumps(payload))
            # mqttc.publish(pubTopic2, pH)
            # mqttc.publish(pubTopic3,round (turb,2))
            print("Published")
            time.sleep(10)

        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
        except Exception as error:
            print("Error encountered!")
            time.sleep(5.0)

    mqttc.loop_forever()


if __name__ == '__main__':
    run()
