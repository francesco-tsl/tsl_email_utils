import os
from contact_email_parser import imap_download
from contact_email_parser import parser


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        msg = "Set the %s environment variable"
        error_msg = msg % var_name
        raise error_msg


def test_imap_parse_messages():

    host = get_env_variable("EMAIL_HOST")
    username = get_env_variable("EMAIL_USERNAME")
    password = get_env_variable("EMAIL_PASSWORD")
    m = imap_download.EMailClient.connect(host,
                                          username,
                                          password, True)

    source = get_env_variable("EMAIL_SOURCE")
    messages = m.fetch_messages(sent_from=source, unread=True)

    assert len(messages) > 0

    for m in messages:
        print "original:", m
        contact = parser.parse(m)
        print "parsed:", contact
        assert 'email' in contact
        assert 'telefono' in contact
        assert 'nome della compagnia' in contact
        assert 'fatturato (reale o stimato)' in contact
        assert 'servizio richiesto' in contact
        assert 'details' in contact
