import json


ROW_LENGTH = 21


def list_all():
    categories = get_categories()
    categories_parsed = ...

def list_only_category() -> str:
    categories = get_categories()
    id_and_name = parse(categories, only_category=True)

    title = get_title("Categories")
    table_header = get_table_header()
    table_rows = get_table_rows(id_and_name)
    
    return "\n".join([title, table_header] + table_rows)


def get_categories() -> list[dict]:
    with open("../../categories.json") as f:
        categories = json.load(f)
        return categories
    
def parse(cs:list[dict], only_category=False):
    if only_category:
        return list(map(parse_one_category, cs))
    return list(map(parse_one, cs))

def parse_one(c:dict) -> tuple:
    if "subcategories" in c:
        return (c["id"], c["name"],
                list(map(parse_one, c["subcategories"])))
    else:
        return (c["id"], c["name"])

def parse_one_category(c):
    return (c["id"], c["name"])

def get_title(name:str) -> str:
    ruler = "="*(len(name) + 1)
    return name + "\n" + ruler

def get_category_header(name:str, row_length:int) -> str:
    rule = "-"*(len(name) + 1)
    return (name.ljust(row_length) +
            "\n" +
            rule.ljust(row_length))

def get_table_header() -> str:
    column_names = (" ID" + " | " + "Name").ljust(ROW_LENGTH)
    ruler = "-"*ROW_LENGTH
    header = column_names + "\n" + ruler
    return header

def get_table_rows(val:list[tuple]) -> list[str]:
    return list(map(get_table_row, val))

def get_table_row(val:tuple) -> str:
    content = val[0].ljust(3) + " | " + val[1]
    return content.ljust(ROW_LENGTH)


"""
Categories
===========
 ID | Name
--------------------
336 | Vehicles
462 | Services
468 | For Rent
 18 | Real Estate
  5 | Community
 17 | Pets
 15 | Jobs
  4 | Items for
    | Sale

All
====
(336) Vehicles       
...............      
ID  | Name           
---------------------
 73 | Aircraft       
462 | Automotive     
    | Items and      
    | Parts          

(468) For Rent       
...............      
ID  | Name           
---------------------
299 | Apartments     
302 | Commercial          
    | Lease
...

    
All
====
(336) Vehicles          (462) Services
...............         ...............
ID  | Name              ID  | Name
---------------------   ---------------------
 73 | Aircraft          467 | Automotive
462 | Automotive            | Services
    | Items and         83  | Beauty & Salon
    | Parts                 | Services

(468) For Rent          (18) Real Estate
...............         .................
ID  | Name              ID  | Name
---------------------   ---------------------
299 | Apartments        301 | Commercial
302 | Commercial            | Real Estate     
    | Lease             312 | Condos For
                            | Sale
...
"""
