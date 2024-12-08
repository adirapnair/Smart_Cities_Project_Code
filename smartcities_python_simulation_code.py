import time
from twilio.rest import Client

# Twilio credentials
ACCOUNT_SID = 'ACb3191805cd1dea2f750e27e046b*****'  # Replace with your Twilio Account SID
AUTH_TOKEN = 'd828846dceeb992b8aa5789332f*****'  # Replace with your Twilio Auth Token
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+141552*****'  # Twilio's WhatsApp sandbox number
TO_WHATSAPP_NUMBER = 'whatsapp:+9181043*****'  # Replace with the verified WhatsApp number

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# User inputs for simulation
limit = int(input("Enter monthly limit (units): "))
alert_1 = int(input("Enter 1st alert level (units): "))
alert_2 = int(input("Enter 2nd alert level (units): "))
alert_3 = int(input("Enter 3rd alert level (units): "))
cutoff = int(input("Enter cutoff threshold (units): "))

# Function to send WhatsApp alert
def send_whatsapp_alert(message):
    client.messages.create(
        body=message,
        from_=TWILIO_WHATSAPP_NUMBER,
        to=TO_WHATSAPP_NUMBER
    )

# Simulate electricity consumption and alerts
consumption = 0
while consumption <= cutoff:
    print(f"Consumed units = {consumption}")
    
    # Check for alerts
    if consumption == alert_1:
        send_whatsapp_alert(f"Alert: You have consumed {alert_1} units out of your {limit} unit limit.")
    elif consumption == alert_2:
        send_whatsapp_alert(f"Alert: You have consumed {alert_2} units out of your {limit} unit limit.")
    elif consumption == alert_3:
        send_whatsapp_alert(f"Alert: Only {limit - alert_3} units left before reaching your monthly limit!")
    elif consumption == limit:
        send_whatsapp_alert("Alert: Monthly limit exhausted. Overusing electricity!")
    elif consumption == cutoff:
        send_whatsapp_alert("Final Alert: Threshold exceeded. Electricity will be cut off.")

    # Increment consumption and add delay for simulation
    time.sleep(1)
    consumption += 5  # Adjust increment as needed