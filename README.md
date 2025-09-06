# Gmail-MCP
MCP Gmail Server + Simple Client
# MCP Gmail Personal App

## Setup

1. Create a Google Cloud Project & enable Gmail API.
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

