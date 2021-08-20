# rkn-monitor

Util for monitoring IP in RKN.

Мониторинг заблокированных РКН IP-адресов можно реализовать с использованием публично доступного API.

Вот список endpoint’ов которые можно дергать:

- `https://api.reserve-rbl.ru/api/v2/json` – общая статистика заблокированных ресурсов, разблокированных, заблокированных за компанию сейчас и разблокированных из заблокированных за компанию по ведомствам в формате JSON;
- `https://api.reserve-rbl.ru/api/v2/csv` – общая статистика заблокированных ресурсов, разблокированных, заблокированных за компанию сейчас и разблокированных из заблокированных за компанию по ведомствам в формате CSV;
- `https://api.reserve-rbl.ru/api/v2/domains/json` – список доменов, находящихся сейчас в реестре в формате JSON;
- `https://api.reserve-rbl.ru/api/v2/ips/json` – список IP-адресов, находящихся сейчас в реестре в формате JSON;
- `https://api.reserve-rbl.ru/api/v2/ips/csv` – список IP-адресов, находящихся сейчас в реестре в формате CSV;
- `https://api.reserve-rbl.ru/api/v2/current/json` – Выдача содержания реестра на текущий момент в формате JSON;
- `https://api.reserve-rbl.ru/api/v2/current/csv` – Выдача содержания реестра на текущий момент в формате CSV;
- `https://api.reserve-rbl.ru/api/v3/current/csv` – Выдача содержания реестра на текущий момент в формате CSV;
- `https://api.reserve-rbl.ru/api/v3/ips-only/json` – Возвращает список IP-адресов, напрямую заблокированных Роскомнадзором (в формате JSON);

Так же присутствует API для поиска. Вы можете экспортировать результат поиска в формате CSV. Для экспорта результатов поиска в CSV, добавьте дополнительный параметр export, принимающий значение records или distributors в URL, как показано ниже.

- `https://reestr.rublacklist.net/export/?q=example.com&export=records` – Ограничить выдачу реестром запрещенных сайтов;
- `https://reestr.rublacklist.net/export/?q=example.com&export=distributors` – Ограничить выдачу реестром ОРИ;

**Важно!** На экспорт результатов поиска установлено ограничение — не более 50 запросов в сутки с одного IP.

Как запускать:

```shell
> python rkn-checker.py check-ipaddr --ipaddr 23.105.247.220
{'status': 'FREE', 'ipaddr': '23.105.247.220'}
```
