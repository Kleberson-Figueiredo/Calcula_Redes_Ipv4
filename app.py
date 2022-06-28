from Classes.CalcIpv4 import CalcIpv4
ip = input("Enter IP address: ")
mask = input("Enter mask: ")
prefixo = int(input("Enter prefix: "))


calc_ipv4 = CalcIpv4(ip=ip, prefixo=prefixo, mascara=mask)

print(f'IP: {calc_ipv4.ip}')
print(f'Máscara: {calc_ipv4.mascara}')
print(f'Redes: {calc_ipv4.rede}')
print(f'Broadcast: {calc_ipv4.broadcast}')
print(f'Prefixo: {calc_ipv4.prefixo}')
print(f'Número de IPs da rede: {calc_ipv4.num_ips}')