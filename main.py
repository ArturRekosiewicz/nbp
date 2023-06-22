import argparse
import datetime
import functools
import nbp


def add_separators(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(50 * '-')
        func(*args, **kwargs)
        print(50 * '-')
    return wrapper


@add_separators
def print_header(rate_table):
    print(f'Tabela: {rate_table.name}\tData: '
          f'{rate_table.effective_date.date()}')


def print_content(rates):
    for rate in rates:
        print(f'{rate.currency}({rate.code})\t{rate.bid_rate}'
              f'\t{rate.ask_rate}')


def print_table(rate_table):
    print_header(rate_table)
    print_content(rate_table.rates())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--date', type=datetime.date.fromisoformat,
                        help='Exchange rate date', default=datetime.date.today().isoformat())
    args = parser.parse_args()
    print_table(nbp.get_exchange_rate_table(args.date.isoformat(), 'json'))
    print(50 * '=')
    print_table(nbp.get_exchange_rate_table(args.date.isoformat(), 'xml'))

