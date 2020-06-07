from socket import *
import threading


def check_port(port):
    s = socket(AF_INET, SOCK_STREAM)

    conn = s.connect_ex((t_IP, port))

    if conn == 0:
        print('Port {}: OPEN'.format(port))
    s.close()


if __name__ == '__main__':
    t_IP = gethostbyname('127.0.0.1')
    print('Set range:')
    try:
        first = int(input('First: '))
        second = int(input('Second: '))
    except ValueError:
        print("Wrong input range, set standard: 50 - 500")
        first = 50
        second = 500

    print('Starting scan')
    for i in range(first, second):
        a = threading.Thread(target=check_port, args=(i,))
        a.start()
        a.join()
