import json


ROW_LENGTH = 22


def list_all():
    categories = get_categories()
    categories_parsed = parse(categories)  # why am I even parsing?

    title = get_title("All")
    subcategories = get_all_subcategories(categories_parsed)

    return "\n\n".join([title] + subcategories)

# list(tuple(name, id, list(tuple(name, id)))) -> list(sections)
# get all subcategory sections in a list
def get_all_subcategories(ls):
    return list(map(get_subcategory, ls))

# tuple(name, id, list(tuple(name, id)))
# get each subcategory section
def get_subcategory(l):
    category_header = get_category_header(l[0], l[1])
    table_header = get_table_header()

    table_rows = get_table_rows(l[2])

    return "\n".join([category_header, table_header] + table_rows)

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

def get_category_header(id:str, name:str) -> str:
    id_and_name = f"({id}) {name}".ljust(ROW_LENGTH)
    rule = "."*(len(id_and_name) + 1)
    return (id_and_name.ljust(ROW_LENGTH) +
            "\n" +
            rule.ljust(ROW_LENGTH))

def get_table_header() -> str:
    column_names = ("  ID" + " | " + "Name").ljust(ROW_LENGTH)
    ruler = "-"*ROW_LENGTH
    header = column_names + "\n" + ruler
    return header

def get_table_rows(val:list[tuple]) -> list[str]:
    return list(map(get_table_row, val))

def get_table_row(val:tuple) -> str:
    name = break_into_groups(val[1].split())
    content = add_rule(name, val[0])
    # content = val[0].ljust(3) + " | " + val[1]
    return "\n".join(content)

def break_into_groups(name:list[str]) -> list[str]:
    groups = []

    lengths = list(map(len, name))
    # print(lengths)
    while len(lengths) != 0:
        # print(len(lengths))
        cumsum = get_altered_cumsum(lengths)
        # print(cumsum)
        last = len(cumsum)
        for i, val in enumerate(cumsum):
            if val > 15:
                last = i
                break
        # print(last)
        groups.append(" ".join(name[:last]))
        # print(" ".join(name[:last]))
        # print(groups)
        del lengths[:last]
        del name[:last]

    return groups

def get_altered_cumsum(l):
    # [10, 5, 3, 5] -> [10, 16, 20, 26]

    cumsum = [sum(l[:i])+(i-1) for i in range(1, len(l)+1)]
    return cumsum

def add_rule(l, id) -> list[str]:
    l[0] = id.rjust(4) + ' | ' + l[0]

    for i in range(1, len(l)):
        l[i] = "     | " + l[i]

    return l



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
