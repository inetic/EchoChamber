from echochamber.proxy_server import ReorderProxyServer
from echochamber.client import Client
from messaging import MessagingTest
import os

class ReorderTest(MessagingTest):
    def _setup_clients(self):
        self.proxy_servers = []
        for n in range(int(self.test_data["clients"]["count"])):
            account = "client%03d@localhost" % n
            client_data = {
                "account" : account,
                "password" : "password",
                "room" : self.test_data["clients"]["room"],
                "server" : self.test_data["clients"]["server"],
                "port" : 15224 + n }
            self.proxy_servers.append(ReorderProxyServer("localhost", client_data["port"], self.server_host, 5222))
            sock_path = os.path.join(self.sock_path, client_data["account"])
            self.clients.append(Client(client_data, self.config, sock_path, self.debug))
            self._adduser(client_data)

    def run(self):
        for proxy_server in self.proxy_servers:
            proxy_server.communicate()
        super(ReorderTest, self).run()

    def _score(self):
        pass # stubbed

