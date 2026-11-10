# security incident manager

# creates a dictionary containing security incident details
incident = {
    "username": "admin",
    "ip_address": "192.168.1.25",
    "event_type": "Failed login",
    "risk_level": "High"
}

# displays the username and IP address
print("Username: ", incident["username"])
print("IP address: ", incident["ip_address"])

# adds a new field
incident["status"] = "Undercover investigation"

# updates the risk level
incident["risk_level"] = "Critical"

# removes one field
del incident["event_type"]

# displays all remaining keys and values
print(" Incident details: ")

# displays all remaining keys and values
for key, value in incident.items():
    print(key, ":", value)

# displays the number of key-value pairs
print("Total fields: ", len(incident))