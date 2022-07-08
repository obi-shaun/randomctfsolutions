# haxor_server

I often find myself spinning up an out of band web server as part of a solution to a Hack The Box challenge. I usually do this with Flask and Ngrok. 

I use this often when dealing with SSRF or as a detination to exfiltrate data, etc. I set a * CORS header in case the challenge involves a javascript request coming cross origin from a web browser.
