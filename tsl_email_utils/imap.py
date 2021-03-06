# Copyright (c) 2013, Menno Smits
# Released subject to the New BSD License
# Please see http://en.wikipedia.org/wiki/BSD_licenses

from __future__ import unicode_literals
from imbox import Imbox


default_filter = lambda msgid, msg: (msgid, msg)


class EMailClient(Imbox):

    @classmethod
    def connect(cls, host, username, password, ssl_enabled):
        return cls(host, username, password, ssl=ssl_enabled)

    def fetch_bodies_plain(self, **imap_filters):
        func = lambda _, msg: msg.body['plain'][0]

        return [m for m in self.fetch_messages(func, True, **imap_filters)]

    def fetch_messages(self, filter_func, mark_seen, **imap_filters):
        response = self.messages(**imap_filters)
        func = filter_func or default_filter
        for msgid, msg in response:

            res = func(msgid, msg)
            if mark_seen:
                try:
                    self.mark_seen(msgid)
                except Exception as e:
                    print(e)

            if res:
                yield res
