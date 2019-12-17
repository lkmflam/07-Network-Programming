Downloading web pages
The basic ability to download a web page involves making an HTTP GET request against a URL. This is the basic operation of any web browser. Let's quickly recap the different parts of this operation:

Using the HTTP protocol.
Using the GET method, which is the most common HTTP method. We'll see more in the Accessing web APIs recipe.
URL describing the full address of the page, including the server and the path.
That request will be processed by the server and a response will be sent back. This response will contain a status code, typically 200 if everything went fine, and a body with the result, which will normally be text with an HTML page.

Most of this is handled automatically by the HTTP client used to perform the request. We'll see in this recipe how to make a simple request to obtain a web page.

HTTP requests and responses can also contain headers. Headers contain extra information, such as the total size of the request, the format of the content, the date of the request, and what browser or server is used. 
