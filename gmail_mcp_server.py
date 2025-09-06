from gmail_mcp_server import GmailMCPServer

# Path to OAuth credentials from Step 1
creds_path = "credentials.json"
token_path = "token.json"

server = GmailMCPServer(
    creds_path=creds_path,
    token_path=token_path
)
server.start()  # Starts default MCP server at http://localhost:3845/mcp
