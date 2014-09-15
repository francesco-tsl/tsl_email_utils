import os
import pytest
from tsl_email_utils import imap


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        msg = "Set the %s environment variable"
        error_msg = msg % var_name
        raise Exception(error_msg)


@pytest.fixture
def imap_client():

    host = get_env_variable("EMAIL_HOST")
    username = get_env_variable("EMAIL_USERNAME")
    password = get_env_variable("EMAIL_PASSWORD")
    return imap.EMailClient.connect(host,
                                    username,
                                    password, True)


def test_imap_parse_messages(imap_client):

    source = get_env_variable("EMAIL_SOURCE")
    messages = imap_client.fetch_bodies_plain(sent_from=source)

    assert len(messages) > 0
    assert messages[0] == "this is a message\r\n"


def test_fetch_messages_with_default_filter(imap_client):

    source = get_env_variable("EMAIL_SOURCE")
    func = imap.default_filter
    messages = imap_client.fetch_messages(func, False, sent_from=source)

    for m in messages:
        assert len(m) == 2


def test_fetch_messages_with_custom_filter(imap_client):

    source = get_env_variable("EMAIL_SOURCE")
    func = lambda _, msg: {'subject': msg.subject,
                           'attachments': msg.attachments
                           }
    messages = imap_client.fetch_messages(func, False, sent_from=source)

    for m in messages:
        assert m['subject'] == '012345'
        filename = '"Schermata 2014-09-03 alle 21.46.18.png"'
        assert m['attachments'][0]['filename'] == filename
