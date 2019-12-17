Identifying URL-based SQLi
So, we've looked at fuzzing before for XSS and error messages. This time, we're doing something similar but with SQL Injection, instead. The crux of any SQLi starts with a single quotation mark, tick, or apostrophe, depending on your personal choice of word. We throw a tick into the URL targeted and check the response to see what version of SQL is running if successful.

We will create a script that sends the basic SQL Injection string to our targeted URL, record the output, and compare to known phrases in error messages to identify the underlying system.
