import sys
import click
import requests


URL_BLOCKED_IPS = 'https://api.reserve-rbl.ru/api/v2/ips/json'


def get_ips_only_list(url: str) -> dict:
    res = requests.get(url=url)
    if res.status_code == 200:
        return res.json()
    return None


def validate_ipaddr(ip: str, ipadds_list: list):
    """Если переданный IP не глобальный - проверка провалена"""
    if ip in ipadds_list:
        return True
    return False


@click.command()
@click.option('--ipaddr', required=True, help='IP address for check in RKN')
def check_ipaddr(ipaddr: str):
    ips_list = get_ips_only_list(URL_BLOCKED_IPS)
    if ips_list:
        if validate_ipaddr(ip=ipaddr, ipadds_list=ips_list):
            sys.stdout.write(str({
                'status': 'BLOCKED',
                'ipaddr': ipaddr,
            }))
        else:
            sys.stdout.write(str({
                'status': 'FREE',
                'ipaddr': ipaddr,
            }))


@click.group()
def cli():
    pass


cli.add_command(check_ipaddr)

if __name__ == '__main__':
    cli()
