Ref: https://www.dj4e.com/lessons/rrc#

# Introduction to Dynamic Web Content

## The Structure

- Browser -> Internet -> Web Server

Front End Tech -> Browser (HTML, CSS, DOM, JavaScript, Jquery)
Internet
Back End Tech -> Django / Flask & Sqlite3 / MySQL

## Getting Data from the Server

- By clicking on a link or anchor tag with an href = value, the browser makes a new connection to the web server and issues a GET request - to get the content of the page specified URL

- Then, the server return the HTML document to the browser, which formats and displays the document to the user

- The get and response between the server and the browser is made by the connection socket

## HypeText Transfer Protocol

- Protocol browsers uses to "talk" to servers

- Allows for multiple protocols (http being the most used)

- Uniform Resourse Locator (URL)

http:// || data.pr4e.org || /pagel.htm
protocol||      host     || document

- Basic COncept: Makes a connection - Request a document - Retrieve the document - Close the connection

- Invented in 1990 and is an application protocol that runs atop sockets

## Internet Standards

- IPV6

- Standards for all of the internet protocols (inner workings) are developed by an organization

- Internet Engineering Task Force (IETF)

- www.ietf.org

- Documentation is free and available to acess by anyone

## Making an HTTP Request

- Connect to the server -> a "handshake" -> request a document

## Network Sockets (phone calls for pairs of applications)

- TCP Connections / Sockets

- In computer networking, an Internet socket or networkj socket is an endpoint of bidirectional inter-process communication flow across an Internet Protocol-based computer network, such as the Internet

- Application Process <-> Internet <-> Application Process

## TCP Port Numbers

- A port is an application-specific or process-specific software communication endpoint

- it allows multiple networked applications to coexist on the same server

- there is a list of well-known TCP port numbers

- Ex: 25 (incoming email), 23 (Login), 80 (Webserver-unsecure), 443 (webserver)

- each port has its own protocol

# simpleBrowser.py example

# simpleServer.py example











