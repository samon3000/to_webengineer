import re
import traceback
from datetime import datetime
from socket import socket
from threading import Thread
from typing import Tuple

import settings
from ajango.http.request import HTTPRequest
from ajango.http.response import HTTPResponse
from ajango.urls.resolver import URLResolver


class Worker(Thread):
    # 拡張子とMIME Type
    MIME_TYPES = {
        "html": "text/html; charset=UTF-8",
        "css": "text/css",
        "png": "image/png",
        "jpg": "image/jpg",
        "gif": "image/gif",
    }

    # ステータスコードとステータスライン
    STATUS_LINES = {
        200: "200 OK",
        302: "302 Found",
        404: "404 Not Found",
        405: "405 Method Not Allowed",
    }

    PORT_NUM = 0

    def __init__(self, client_socket: socket, address: Tuple[str, int]):
        super().__init__()
        self.PORT_NUM = address[1]

        self.client_socket = client_socket
        self.client_address = address

    def run(self) -> None:
        """
        クライアントと接続済みのsocketを引数として受け取り、
        リクエストを処理してレスポンスを送信する
        """

        try:

            # クライアントから送られてきたデータを取得する
            request_bytes = self.client_socket.recv(4096)

            # クライアントから送られてきたデータをファイルに書き出す
            with open(f"{settings.BASE_DIR}/server_log/webserver_recv{self.PORT_NUM}.txt", "wb") as f:
                f.write(request_bytes)

            # リクエストをパースする
            request = self.parse_http_request(request_bytes)

            view = URLResolver().resolve(request)

            response = view(request)

            if isinstance(response.body, str):
                response.body = response.body.encode()
            
            response_line = self.build_response_line(response)
            # レスポンスヘッダーを生成
            response_header = self.build_response_header(response, request)

            # レスポンス全体をまとめてBytes型にする
            response_bytes = (response_line + "\r\n" + response_header + "\r\n").encode() + response.body

            # クライアントへレスポンスを送信する
            self.client_socket.send(response_bytes)

        except Exception:
            # リクエストの処理中に例外が発生した場合はコンソールにエラーログを出力し、
            # 処理を続行する
            print("=== Worker: リクエストの処理中にエラーが発生しました ===")
            traceback.print_exc()

        finally:
            # 例外の発生に関わらず、TCP通信をclose
            print(f"=== Worker: クライアントとの通信を終了します remote_address: {self.client_address} ===")
            self.client_socket.close()
    
    def parse_http_request(self, request: bytes) -> HTTPRequest:
        """
        生のHTTPリクエストをHTTPRequestクラスへ変換する
        """
        # リクエストをパースする
        request_line, remain = request.split(b"\r\n", maxsplit=1)
        request_header, request_body = remain.split(b"\r\n\r\n", maxsplit=1)
        method, path, http_version = request_line.decode().split(" ")

        # リクエストヘッダーを辞書にパースする
        headers = {}
        for header_row in request_header.decode().split("\r\n"):
            key, value = re.split(r": *", header_row, maxsplit=1)
            headers[key] = value

        cookies = {}
        if "Cookie" in headers:
            cookie_strings = headers["Cookie"].split("; ")
            for cookie_string in cookie_strings:
                name, value = cookie_string.split("=", maxsplit=1)
                cookies[name] = value
        return HTTPRequest(method=method, path=path, http_version=http_version, headers=headers, cookies=cookies, body=request_body)

    def build_response_line(self, response: HTTPResponse) -> str:
        # print(response.status_code)
        status_line = self.STATUS_LINES[response.status_code]
        # print(status_code)
        return f"HTTP/1.1 {status_line}"

    def build_response_header(self, response: HTTPResponse, request: HTTPRequest) -> str:
        """
        レスポンスヘッダーを構築する
        """

        # Content-Typeが指定されていない場合はpathから特定する
        if response.content_type is None:
            # pathから拡張子を取得
            if "." in request.path:
                ext = request.path.rsplit(".", maxsplit=1)[-1]
                # 拡張子からMIME Typeを取得
                # 知らない対応してない場合はoctet-streatとする
                response.content_type = self.MIME_TYPES.get(ext, "application/octet-stream")
            else:
                # pathに拡張子がない場合はhtml扱いとする
                response.content_type = "text/html; charset=UTF-8"

        response_header = ""
        response_header += f"Date: {datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}\r\n"
        # response_header += f"Date: {datetime.now(datetime.timezone.utc()).strftime('%a, %d %b %Y %H:%M:%S GMT')}\r\n"
        response_header += "Host: NueServer/0.1\r\n"
        response_header += f"Content-Length: {len(response.body)}\r\n"
        response_header += "Connection: Close\r\n"
        response_header += f"Content-Type: {response.content_type}\r\n"

        # if response.cookies :
        for cookie_name, cookie_value in response.cookies.items():
            response_header += f"Set-Cookie: {cookie_name}={cookie_value}\r\n"

        # if response.headers :
        for header_name, header_value in response.headers.items():
            response_header += f"{header_name}: {header_value}\r\n"

        return response_header