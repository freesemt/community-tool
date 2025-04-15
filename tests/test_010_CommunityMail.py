"""
test_010_CommunityMail.py
"""
import sys
sys.path.insert(0, "..")

def test_010_community_mail():
    """
    Test the CommunityMail class.
    """
    from community_tool.CommunityMail import send_test_mail
    enquete_url = "https://densuke.biz/list?cd=RbBBP5WPSSt3ZTGs"
    return send_test_mail("Test email content", enquete_url=enquete_url)

if __name__ == "__main__":
    bytes = test_010_community_mail()
    print("Test completed successfully. sent bytes:", bytes)