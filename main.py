import sys
from cidrize import cidrize


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


input_file = sys.argv[1]
output_file = sys.argv[2]


def read(input_file):
    # 判断文件是否有带有:的行，如果有则删除，无则直接返回
    with open(input_file, 'r') as f:
        lines = f.readlines()
        if any(':' in line for line in lines):

            lines = [line.strip() for line in lines if ':' not in line]
            return lines
        else:
            return lines
    # # 读取文件并删除带有:的行
    # with open(input_file, 'r') as f:
    #     lines = f.readlines()
    #     lines = [line.strip() for line in lines if ':' not in line]
    # return lines


def ip2cidr(lines):
    # 从文件中读取IP地址并转换为CIDR
    cidrs = []
    for line in lines:
        cidrs.append(cidrize(line))
    return cidrs


def write(output_file, cidrs):
    # 将CIDR写入文件
    with open(output_file, 'w') as f:
        cidrlist = ("\n".join('%s' %id for id in cidrs))
        cidrbf = cidrlist.replace(",", "\n")
        cidr1 = cidrbf.replace("[", "")
        cidr2 = cidr1.replace("]", "")
        cidr3 = cidr2.replace("(", "")
        cidr4 = cidr3.replace(")", "")
        cidr5 = cidr4.replace("'", "")
        cidr6 = cidr5.replace("IPNetwork", "")
        cidr = cidr6.replace(" ", "")

        print(cidr)
        if cidrs == '':
            return 0
        else:
            f.write(str(cidr))
            return 1


def main():
    lines = read(input_file)
    fcidrs = ip2cidr(lines)
    write(output_file, fcidrs)


if __name__ == '__main__':
    main()


