"""
    body = "Hello"
    emailMsg = EmailMessage()
    emailMsg.set_content(body)

    emailMsg["To"] = "@vanderbilt.edu"
    emailMsg["From"] = 'me'
    emailMsg["Subject"] = "OPEN"

    raw = base64.urlsafe_b64encode(emailMsg.as_bytes()).decode()

    send = service.users().messages().send(userId='me',body = {'raw':raw}).execute()

    print(send)

    """