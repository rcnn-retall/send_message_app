
def response(data):
    response_line = "HTTP/1.1 200 OK\r\n".encode("utf8")
    response_header = "Server: PWS/1.1\r\n".encode("utf-8")

    # Server:PWS/1.1
    response = response_line + response_header +"\r\n".encode()+ data+"\r\n".encode("utf8")
    return response

def eooer_response(conde,data):
    response_line = f"HTTP/1.1 {conde} OK\r\n".encode("utf8")
    response_header = "Server: PWS/1.1\r\n".encode("utf-8")

    response = response_line + response_header+"\r\n".encode() + data+"\r\n".encode("utf8")
    return response
