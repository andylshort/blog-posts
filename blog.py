import argparse
from pathlib import Path


BLOG_DIR = Path(__file__).parent / "src" / "pages" / "blog"


def new_blog_post() -> None:
    pass

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser("Blog management")

    commands = parser.add_subparsers()

    cmd_publish = commands.add_parser("new")

    cmd_publish = commands.add_parser("publish")

    cmd_update = commands.add_parser("update")

    return parser

def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    print(args)

if __name__ == "__main__":
    main()
