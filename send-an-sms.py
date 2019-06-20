import nexmo

client = nexmo.Client(key='04893f7a', secret='qpiRMW4Elv3AChe2')

# client.send_message({
#     'from': 'Nexmo',
#     'to': '254774100224',
#     'text': 'Hello from Water',
# })


responseData = client.send_message(
    {
        "from": '0774100224',
        "to": '0708608180',
        "text": "A text message sent using the Nexmo SMS API",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
