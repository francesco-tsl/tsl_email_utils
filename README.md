tsl_email_utils
===============

This package, built on to of Imbox (https://github.com/martinrusev/imbox),
provides some utilities to interact with an imap server.


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
Francesco Pischedda <francesco.pischedda@gmail.com>
The SourceLAB <francesco@thesourcelab.org>
http://francesco.pischedda.info


License
-------
This software is distributed with the BSD 2-Clausole License, please refer to 
LICENSE.txt file or read the description at
http://opensource.org/licenses/bsd-license.php 
