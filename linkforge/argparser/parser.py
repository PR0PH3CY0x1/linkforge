from argparse import ArgumentParser


def parser():
    parser = ArgumentParser(
        prog='escout'
    )

    parser.add_argument(
        '-u',
        '--url'
    )

    parser.add_argument(
        '-n',
        '--max'
    )
    

    args = parser.parse_args()

    return args
