# SMTP

### Simple Mail Transfer Protocol

Most of the internet systems use SMTP as a method to transfer mail from one user to another. SMTP is a push protocol and is used to send the mail whereas POP \(post office protocol\) or IMAP \(internet message access protocol\) are used to retrieve those emails at the receiver’s side.

 SMTP communication between mail servers uses TCP port 25. Mail clients on the other hand, often submit the outgoing emails to a mail server on port 587 or 465. The latter port was previously deprecated, but this changed with [RFC 8314](https://tools.ietf.org/html/rfc8314) and its use is now recommended to ensure security. SMTP connections on port 25 or 587 can be secured using an extra command \([STARTTLS](https://en.wikipedia.org/wiki/Opportunistic_TLS)\).

![](../.gitbook/assets/image%20%283%29.png)

**SMTP Fundamentals**  
 SMTP is an application layer protocol. The client who wants to send the mail opens a TCP connection to the SMTP server and then sends the mail across the connection. The SMTP server is always on listening mode. As soon as it listens for a TCP connection from any client, the SMTP process initiates a connection on that port \(25\). After successfully establishing the TCP connection the client process sends the mail instantly.

**SMTP Protocol**

The SMTP model is of two type :

1. End-to- end method
2. Store-and- forward method

The end to end model is used to communicate between different organizations whereas the store and forward method is used within an organization. A SMTP client who wants to send the mail will contact the destination’s host SMTP directly in order to send the mail to the destination. The SMTP server will keep the mail to itself until it is successfully copied to the receiver’s SMTP.  
 The client SMTP is the one which initiates the session let us call it as client- SMTP and the server SMTP is the one which responds to the session request and let us call it as receiver-SMTP. The client- SMTP will start the session and the receiver-SMTP will respond to the request.
