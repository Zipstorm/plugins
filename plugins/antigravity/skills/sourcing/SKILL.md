---
name: sourcing
description: Find candidates for a recruiting role in SeekOut. Use when the recruiter asks to find people or supplies a role in response to the Find candidates starter.
---

Use the recruiter's words and the preceding turn to establish their intent. If a fresh conversation contains only a role such as “CFO”, ask what the recruiter wants to do and wait for their answer.

After the recruiter sends **Find candidates**, ask for the role if it is missing. Once they give a title, run the search on that turn. Honor any other constraints they gave. Leave unspecified preferences open.

Use the installed SeekOut plugin's MCP connection and its `search_candidates` tool. Check the tool's input schema and use the server's recruiting guidance for supported search fields. If the plugin connection needs sign-in, direct the recruiter to **Customizations → Installed → SeekOut → Accounts**. If the tool is unavailable, tell the recruiter which connection needs attention.

Show a short list drawn from the returned profiles and identify the criteria used. If the service reports an unknown search outcome, give the recruiter the request ID and explain that a repeated search may count again. Wait for their instruction before retrying.
