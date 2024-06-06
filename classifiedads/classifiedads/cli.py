from argparse import ArgumentParser


parser = ArgumentParser(description="Scraper for ClassifiedAds.com")
subparser = ArgumentParser.add_subparsers(parser, help="subparsers help")

scrape_subparser = subparser.add_parser("scrape", help="scrape help")
scrape_subparser.add_argument("id", help="id help")
scrape_subparser.add_argument("-f", "--format", help="format help")

categories_subparser = subparser.add_parser("categories", help="categories help")
categories_subparser.add_argument("-a", "--all", help="all help")

parser.parse_args()

print("Done")
