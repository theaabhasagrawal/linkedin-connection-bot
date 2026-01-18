import asyncio
import argparse

from app.login import login
from app.connect import run_connect_flow
from app.config_loader import load_config


def parse_args():
    parser = argparse.ArgumentParser(
        description="LinkedIn Connection Automation Bot"
    )

    parser.add_argument(
        "--query",
        help="Search keyword (overrides config.yaml)",
        type=str
    )

    parser.add_argument(
        "--limit",
        help="Max connection requests (overrides config.yaml)",
        type=int
    )

    parser.add_argument(
        "--start-page",
        help="Start page number",
        type=int
    )

    parser.add_argument(
        "--max-pages",
        help="Max pages to scan",
        type=int
    )

    return parser.parse_args()


def apply_cli_overrides(config, args):
    # Search overrides
    if args.query:
        config["search"]["query"] = args.query

    if args.start_page is not None:
        config["search"]["start_page"] = args.start_page

    if args.max_pages is not None:
        config["search"]["max_pages"] = args.max_pages

    # Limits overrides
    if args.limit is not None:
        config["limits"]["max_requests"] = args.limit

    return config


async def main():
    args = parse_args()
    config = load_config()
    config = apply_cli_overrides(config, args)

    _, _, _, page = await login()
    await run_connect_flow(page, config)


if __name__ == "__main__":
    asyncio.run(main())
