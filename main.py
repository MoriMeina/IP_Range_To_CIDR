import ipaddress
import sys
import threading


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


input_file = sys.argv[1]
output_file = sys.argv[2]


def calculation(ip_range):
    first, last = ip_range.split('-')
    start_ip = ipaddress.IPv4Address(first)
    end_ip = ipaddress.IPv4Address(last)
    ip_network = ipaddress.summarize_address_range(start_ip, end_ip)
    for network in ip_network:
        return str(network)


def read_file(input_file):
    # 判断文件是否有带有:的行，如果有则删除，无则直接返回
    with open(input_file, 'r') as f:
        lines = f.readlines()
        if any(':' in line for line in lines):
            lines = [line.strip() for line in lines if ':' not in line]
            return lines
        else:
            return lines


def ip2cidr(lines, output_file):
    with open(output_file, 'w') as f:
        for line in lines:
            cidr = calculation(line)
            f.write(cidr + '\n')
            print(output_file + ':' + cidr)


def main():
    lines = read_file(input_file)
    ip2cidr(lines, output_file)


if __name__ == '__main__':
    main()
