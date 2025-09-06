import requests

MCP_SERVER = "http://localhost:3845/mcp"

def get_unread_emails():
    response = requests.get(f"{MCP_SERVER}/emails?filter=unread")
    emails = response.json()
    return emails

def send_reply(email_id, reply_text):
    payload = {
        "email_id": email_id,
        "message": reply_text
    }
    response = requests.post(f"{MCP_SERVER}/send_reply", json=payload)
    return response.ok

def main():
    print("Fetching unread emails...")
    unread_emails = get_unread_emails()

    for email in unread_emails:
        print(f"From: {email['from']}, Subject: {email['subject']}")
        # Simulate quick reply to first email
        if email == unread_emails[0]:
            reply_text = "Thanks for your email! I will get back to you shortly."
            success = send_reply(email['id'], reply_text)
            if success:
                print("Sent quick reply!")
            else:
                print("Failed to send reply.")
            break

if __name__ == "__main__":
    main()
