tsl_email_utils
===============

This package, built on top of Imbox (https://github.com/martinrusev/imbox),
provides some utilities to interact with an imap server.


History
-------

One day you are creating a software to fetch new contact requests sent from a
website form, the day after you have to fetch attachments to feed another
application and so on...so you realize that there is some common code that you
want to keep somewhere


Basic usage
-----------

This package provides a class EmailClient that extends Imbox providing:
* a static method method "connect" that creates an EmailClient object
  representing a connection
* a method "fetch_messages" that retrieve messages with optional Imbox filters;
  by default this returns an iterable of tuples such as (msgid, message) but,
  if a callback function is provided, the elements of the iterable is defined by
  the return value of the callback; if mark_seen is True the message will be
  marked as seen.

Please have a look at the tests to see "real" usage


Author
------
The SourceLAB <francesco@thesourcelab.org>
=======
Francesco Pischedda <francesco@thesourcelab.org>
http://www.thesourcelab.org


License
-------
This software is distributed with the BSD 2-Clausole License, please refer to 
LICENSE.txt file or read the description at
http://opensource.org/licenses/bsd-license.php 
