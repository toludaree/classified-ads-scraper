from argparse import ArgumentParser
from category import list_all, list_only_category
from scrape import scrape_data


def handle_category_group(args):
    if args.only_category is True:
        print(list_only_category())
    else:
        print(list_all())

def handle_scrape_group(args):
    scrape_data(args.id)


parser = ArgumentParser(description="Scraper for ClassifiedAds.com")
subparser = ArgumentParser.add_subparsers(parser)

scrape_subparser = subparser.add_parser("scrape", help="Scrape a particular category or subcategory")
scrape_subparser.add_argument("id", help="Category or Subcategory ID. Run ... to confirm ID")
scrape_subparser.add_argument("-f", "--format", help="file format to save results to. Choose one of json, xml, csv")
scrape_subparser.set_defaults(func=handle_scrape_group)

categories_subparser = subparser.add_parser("categories", help="List the IDs and Names of categories and/or subcategories")
category_group = categories_subparser.add_mutually_exclusive_group()
category_group.add_argument("-a", "--all", help="List all category and subcategory names and their ids", action="store_true")
category_group.add_argument("-c", "--only-category", help="List all category names and their ids", action="store_true")
category_group.set_defaults(func=handle_category_group)

args = parser.parse_args()
args.func(args)