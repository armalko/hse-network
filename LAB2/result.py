import argparse
import subprocess
import ipaddress
import validators


def init_check(host):
    pr = subprocess.run(
        ['cat', '/proc/sys/net/ipv4/icmp_echo_ignore_all'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if pr.stdout == 1:
        print('Error: ICMP')
        exit(1)

    pr = subprocess.run(
        ["ping", host, '-M', 'do', '-s', '0', '-c', '1'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if pr.returncode != 0:
        print('Error: host do not response')
        exit(1)


def parse_mtu(host):
    init_check(host)

    lb = 0
    rb = 8973

    while lb != rb and lb < rb - 1:
        mid = (lb + rb) // 2

        pr = subprocess.run(
            ["ping", host, '-M', 'do', '-s', str(mid), '-c', '5'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        code = pr.returncode

        if code == 0:
            lb = mid
        elif code == 1:
            rb = mid
        else:
            print('Error: ping not working')
            exit(1)

    return lb


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('host')
    args = parser.parse_args()
    host = args.host

    if not validators.domain(host):
        try:
            ipaddress.ip_address(host)
        except Exception:
            print('Error: invalid host entered')
            exit(1)

    res = parse_mtu(host) + 28
    print(f'MTU: {res}')


if __name__ == '__main__':
    main()
