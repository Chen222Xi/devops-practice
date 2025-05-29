import os
import subprocess

def ping(host):
    result = subprocess.run(
        'ping -c2 %s > /dev/null' % host,
        shell=True
    )
    if result.returncode == 0:
        print('%s : up' % host)
    else:
        print('%s : down' % host)

if __name__ == '__main__':
    # 替换为你当前所在网段
    ips = ['192.168.86.%s' % i for i in range(1, 255)]

    for ip in ips:
        ret_val = os.fork()
        if not ret_val:
            ping(ip)
            exit()


# import os
# import platform
# import multiprocessing

# def ping(ip):
#     param = "-n" if platform.system().lower() == "windows" else "-c"
#     command = f"ping {param} 1 {ip} > /dev/null 2>&1"
#     result = os.system(command)
#     if result == 0:
#         print(f"[+] {ip} is up")
#     else:
#         print(f"[-] {ip} is down")

# def main():
#     base_ip = "192.168.86."  # 你的局域网前缀
#     ip_list = [base_ip + str(i) for i in range(1, 255)]

#     print("🔍 正在扫描局域网设备，请稍候...\n")
#     with multiprocessing.Pool(processes=20) as pool:
#         pool.map(ping, ip_list)

# if __name__ == "__main__":
#     main()

