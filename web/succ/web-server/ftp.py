import socket
from pathlib import Path


class FtpException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class FtpClient:
    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._is_connected = False
        self._is_logged_in = False

    def _recv_reply(self) -> tuple[int, str]:
        code, text = self._sock.readline().decode().split(maxsplit=1)
        return int(code), text

    def _send_cmd(self, command: str, arg: str | None = None):
        line = command
        if arg:
            line += f" {arg}"
        line += "\r\n"
        self._sock.write(line.encode())

    def _check_connected(self):
        if not self._is_connected:
            raise FtpException("connection not established")

    def _check_logged_in(self):
        self._check_connected()
        if not self._is_logged_in:
            raise FtpException("connection not logged in")

    def _pasv(self) -> tuple[str, int]:
        self._send_cmd("PASV")
        code, text = self._recv_reply()
        if code // 100 != 2:
            raise FtpException(f"error: {code} {text}")

        components = text.split("(")[1].split(")")[0].split(",")
        ip = ".".join(components[:4])
        port = int(components[4]) * 256 + int(components[5])

        return ip, port

    def _data_stream(self) -> socket.SocketIO:
        ip, port = self._pasv()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        return socket.SocketIO(sock, "rw")

    def connect(self):
        if self._is_connected:
            raise FtpClient("connection already established")

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self._host, self._port))
        self._sock = socket.SocketIO(sock, "rw")

        code, text = self._recv_reply()
        if code // 100 == 2:
            self._is_connected = True
            return
        elif code // 100 != 1:
            raise FtpClient(f"unexpected ready code: {code} {text}")

        code, text = self._recv_reply()
        if code // 100 != 2:
            raise FtpClient(f"unexpected ready code: {code} {text}")

        self._is_connected = True

    def login(self, username: str, password: str):
        self._check_connected()

        self._send_cmd("USER", username)
        code, text = self._recv_reply()
        if code // 100 == 2:
            return
        elif code // 100 != 3:
            raise FtpException(f"login error: {code} {text}")

        self._send_cmd("PASS", password)
        code, text = self._recv_reply()
        if code // 100 != 2:
            raise FtpException(f"login error: {code} {text}")

        self._is_logged_in = True

    def working_directory(self) -> str:
        self._check_logged_in()

        self._send_cmd("PWD")
        code, text = self._recv_reply()
        if code // 100 != 2:
            raise FtpException(f"error: {code} {text}")

        return text.split('"')[1]

    def list_files(self, path: Path | None = None) -> list[str]:
        self._check_logged_in()

        with self._data_stream() as ds:
            self._send_cmd("LIST", path)
            code, text = self._recv_reply()
            if code // 100 != 1:
                raise FtpException(f"error: {code} {text}")

            code, text = self._recv_reply()
            if code // 100 != 2:
                raise FtpException(f"error: {code} {text}")

            lines = ds.readall().decode().splitlines()

        return lines

    def upload_file(self, local_path: Path, remote_path: Path):
        self._check_logged_in()

        with open(local_path, "rb") as f, self._data_stream() as ds:
            self._send_cmd("STOR", str(remote_path))
            code, text = self._recv_reply()
            if code // 100 != 1:
                raise FtpException(f"error: {code} {text}")

            data = f.read()
            while len(data) > 0:
                written = ds.write(data)
                data = data[written:]

        code, text = self._recv_reply()
        if code // 100 != 2:
            raise FtpException(f"error: {code} {text}")
