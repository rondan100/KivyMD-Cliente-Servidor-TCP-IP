import socket


def cliente(self, soquete):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))
    # full_msg = ''
    # msg = s.recv(16)
    # full_msg += msg.decode("utf-8")

    # if len(full_msg) > 0:
    #     print(full_msg)

    s.send(bytes("Cliente enviouuu!!!", "utf-8"))
    s.close()
    self.alert_dialog.dismiss()
