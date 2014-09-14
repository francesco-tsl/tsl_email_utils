# Copyright (c) 2013, Menno Smits
# Released subject to the New BSD License
# Please see http://en.wikipedia.org/wiki/BSD_licenses

from __future__ import unicode_literals
from imbox import Imbox


class EMailClient(Imbox):

    @classmethod
    def connect(cls, host, username, password, ssl_enabled):
        return cls(host, username, password, ssl=ssl_enabled)

    def fetch_messages(self, **filters):
        message_text = []
        response = self.messages(**filters)
        for msgid, msg in response:

            text = msg.body['plain'][0]

            message_text.append(text)
            self.mark_seen(msgid)

        return message_text
