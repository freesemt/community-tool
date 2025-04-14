"""
CommunityMail.py
"""
import os
import yagmail

MY_GMAIL_ADDRESS = os.getenv("MY_GMAIL_ADDRESS")
MY_GMAIL_PASSWORD = os.getenv("MY_GMAIL_PASSWORD")
COMMUNITY_ADDRESS = os.getenv("COMMUNITY_ADDRESS")

SEND_ADDRESS = MY_GMAIL_ADDRESS.replace("@gmail.com", "+community_send@gmail.com")
RECEIVE_ADDRESS = MY_GMAIL_ADDRESS.replace("@gmail.com", "+community_receive@gmail.com")

def send_test_mail(mail_content, phone_number=None):
    """
    Function to send mail content.
    """
    # Initialize the yagmail client
    yag = yagmail.SMTP(SEND_ADDRESS, MY_GMAIL_PASSWORD)

    if phone_number is None:
        recipient = COMMUNITY_ADDRESS
    else:
        recipient = f"{phone_number}@docomo.ne.jp"
    subject = "4/15 電子回覧試験メール（テスト）"
    html_content = f"""
    クリックして、事務局宛てに状況を送信してください。
    <ol>
    <li><a href="mailto:自治会事務局宛て<{RECEIVE_ADDRESS}>?subject=電子回覧受信連絡&body=4/15 電子回覧を受信しました。">受信連絡（返信必須：そのままの内容で送信）</a></li>
    <li><a href="https://densuke.biz/list?cd=prqvDkGC4VfBN7AV">伝助いいねアンケート（回答任意）</a></li>
    </ol>
    """

    # Send the email
    yag.send(
        to=recipient,
        subject=subject,
        contents=html_content
    )

    return utf8_length_in_bytes(html_content)

def utf8_length_in_bytes(input_string):
    """
    Calculate the length of a string in bytes when encoded in UTF-8.
    :param input_string: The string to calculate the byte length for.
    :return: The length of the string in bytes.
    """
    return len(input_string.encode('utf-8'))