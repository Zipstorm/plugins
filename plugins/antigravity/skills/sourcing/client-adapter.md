# Using SeekOut in Antigravity

Use the SeekOut MCP connection supplied by the installed plugin. For setup choices, use a question control when the host offers one, or ask in chat. The Find candidates starter asks its one role question in chat.
Present results from the returned records and links. When an inline view shows the records,
summarize the scope and findings in chat. When the client displays text only, include a short
list with each person's name, current role, company and returned link where available.
Use other connections only when the necessary action is available in this conversation.

## Find candidates in Antigravity

Use the recruiter's words and the preceding turn to establish their intent. If a fresh conversation contains only a role such as “CFO”, ask what the recruiter wants to do and wait for their answer.

After the recruiter sends **Find candidates**, ask for the role if it is missing. Once they give a title, run the search on that turn. Honor any other constraints they gave. Leave unspecified preferences open.

Use the installed SeekOut plugin's MCP connection and its `search_candidates` tool. Check the tool's input schema and use the server's recruiting guidance for supported search fields. If the plugin connection needs sign-in, use the current client’s account controls. In Antigravity, open **Customizations → Installed → SeekOut → Accounts**. If the tool is unavailable, tell the recruiter which connection needs attention.

Show a short list drawn from the returned profiles and identify the criteria used. If the service reports an unknown search outcome, give the recruiter the request ID and explain that a repeated search may count again. Wait for their instruction before retrying.
