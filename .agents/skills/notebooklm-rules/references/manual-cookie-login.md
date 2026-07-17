# Troubleshooting & Manual Cookie Login Guide

When Google invalidates cookies (usually every 2–4 weeks), commands will fail with `Authentication expired` or `Failed to authenticate session`.

## Verification of Authentication
Run the diagnostic command in the terminal to verify active profiles and credentials:
```bash
nlm login --check
```

## Manual Cookie Extraction Steps
1. Log in to [https://notebooklm.google.com](https://notebooklm.google.com) in your web browser.
2. Open **Developer Tools** (`F12` or `Ctrl+Shift+I`).
3. Select the **Network** tab and filter by `batchexecute`.
4. Click on any notebook in the UI to trigger a background request.
5. Left-click the `batchexecute` request list item on the left.
6. In the right-hand details panel, select the **Headers** tab, scroll to **Request Headers**, and find `cookie:`.
7. Select the entire long cookie string, copy it, and paste it into a temporary local file (e.g., `cookie.txt`).
8. Run the CLI command:
   `nlm login --manual --file <path_to_cookie.txt>`
9. Delete the temporary `cookie.txt` file immediately for safety.
