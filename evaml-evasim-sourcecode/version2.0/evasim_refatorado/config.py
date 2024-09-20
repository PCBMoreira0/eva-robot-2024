# Smart Bulb Adress
SMART_BULB_IP_ADRESS = '192.168.99.105' # 
SMART_BULB_PORT      = 55443


# MQTT Broker configuration
# Note: All robots (EVA and FRED) will access the broker through the IP 192.168.99.100
MQTT_BROKER_ADRESS      = '127.0.0.1' # Acer Laptop IP address # Ip adress (Fred router) 192.168.99.100
MQTT_PORT               = 1883
ROBOT_TOPIC_BASE        = 'EVA' # You can change it if you wish to use another robot such as FRED
SIMULATOR_TOPIC_BASE    = 'SIM'

# Default audio file extension.
AUDIO_EXTENSION = ".wav"

# Audio format generated by IBM Watson (file extension).
WATSON_AUDIO_EXTENSION = ".mp3"
ACCEPT_AUDIO_EXTENSION = "audio/mp3"

# Default voice (language) for the IBM Watson service.
VOICE_TONE = "pt-BR_IsabelaV3Voice" 