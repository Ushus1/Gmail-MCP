# Gmail-MCP
MCP Gmail Server + Simple Client
# MCP Gmail Personal App

## Setup

1. Create a Google Cloud Project & enable Gmail API.
     Go to Google Cloud Console.
     Create a new project (or select an existing one).
     Navigate to APIs & Services > Library and enable Gmail API.
     Go to APIs & Services > Credentials.
     Click Create Credentials > OAuth client ID.
     Choose Desktop app, give it a name, and create.
     Download the generated credentials.json file. This will be used by your MCP Gmail server to authenticate.
2. Create OAuth credentials (Desktop App) and download `credentials.json`.
3. Place `credentials.json` in this folder.
4. Install dependencies:
    pip install -r requirements.txt
5. Start the MCP Gmail server:
python gmail_mcp_server.py

6. Authorize Gmail access when the browser opens.
7. In a new terminal, run:
python gmail_client.py

8. See unread emails summary and send a quick reply.

## Description

- `gmail_mcp_server.py` runs the MCP Gmail server exposing your Gmail inbox.
- `gmail_client.py` is a simple client showing how to fetch unread emails & send quick replies using MCP.

- Repo
mcp-gmail-personal-app/
credentials.json           # Your Google OAuth2 credentials (downloaded from Google Cloud)
token.json                 # Automatically created after first auth
gmail_mcp_server.py        # MCP Gmail Server code (runs MCP server)
gmail_client.py            # Simple MCP client to fetch & reply emails
README.md                  # Setup and usage instructions
requirements.txt           # Python dependencies

