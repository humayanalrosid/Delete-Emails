# Delete Unread Emails

Are you as lazy as I am, gathering an alot of useless emails in your inbox that you never bother to read?

Take a look at my Python script if you don't want to delete by picking 50 at once.

## Requirements
1. **Python 3** installed on your system
2. Install **IMAPClient**
   * pip install imapclient
## Enable IMAP 
1. To enable IMAP,
    - In the top right, click **Settings** > See all settings
    - Click the Forwarding and **POP/IMAP** tab.
    - In the **"IMAP access"** section, select **Enable IMAP**.
    - Click **Save Changes**.

## Create App Password
1. Sign in to your Gmail account.
2. [Check this link](https://support.google.com/mail/answer/185833?hl=en-GB)
3. [Go to Your Account](https://myaccount.google.com/)
4. On the left navigation panel, choose **Security**.
5. In the Security section, looks for **App passwords** under **Signing in to Google** section.
**[Make sure that 2-Step Verification is on]**
6. Click on **App Passwords**.
7. Select **Other Custom Name**.
8. Generate an App by the name **My App**.
9. Now Copy the generated App Password and use it on you python script to access your Gmail account.

