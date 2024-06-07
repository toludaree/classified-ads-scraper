import json


def list_only_category():
    categories = get_categories()
    id_and_name = parse_categories(categories)

    length = 21

    headers = [get_general_header("Categories"),
               get_table_header(length)]
    # general_header = get_general_header("Categories")
    # table_header = get_table_header(length)
    table_rows = get_table_rows(id_and_name, length)
    headers.extend(table_rows)

    return "\n".join(headers)


def get_categories() -> list[dict]:
    with open("../../categories.json") as f:
        categories = json.load(f)
        return categories
    
def parse_categories(cs:list[dict]) -> list[tuple]:
    return list(map(parse_category, cs))

def parse_category(c:dict) -> tuple:
    return (c["id"], c["name"])

def get_general_header(name:str) -> str:
    rule = "="*(len(name) + 1)
    return name + "\n" + rule

def get_category_header(name:str, row_length:int) -> str:
    rule = "-"*(len(name) + 1)
    return (name.ljust(row_length) +
            "\n" +
            rule.ljust(row_length))

def get_table_header(row_length:int) -> str:
    header = (" ID" + " | " + "Name").ljust(row_length)
    rule = "-"*row_length
    return header + "\n" + rule

def get_table_rows(val:list[tuple], length:int) -> list[str]:
    return list(map(lambda val: get_table_row(val, length), val))

def get_table_row(val:tuple, row_length:int) -> str:
    content = val[0].ljust(3) + " | " + val[1]
    return content.ljust(row_length)


"""
Categories
===========
 ID | Name
---------------------
336 | Vehicles
462 | Services
468 | For Rent
 18 | Real Estate
  5 | Community
 17 | Pets
 15 | Jobs
  4 | Items for Sale

Sub-Categories
===============
Vehicles                            Services 
.........                           .........
ID  | Name                          ID  | Name
---------------------------------   -----------------------------
 73 | Aircraft                      467 | Automotive Services
462 | Automotive Items and Parts     83 | Beauty & Salon Services

For Rent                            Real Estate
.........                           ............
ID  | Name                          ID  | Name
-----------------------             -----------------------------
299 | Apartments                    301 | Commercial Real Estate
302 | Commercial Lease              312 | Condos For Sale
...
"""

"""
Categories
- title
- content

title 
"""
