import json


# def list_only_category():
#     with open("../categories.json") as f:
#         categories = json.load(f)
    
#     length = 21
#     title_name = "Categories"
#     title = title_name + "\n" + "="*(len(title_name) + 1) + "\n"

#     table_header = ...

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

def get_table_row(id:str, name:str, row_length:int) -> str:
    content = id.ljust(3) + " | " + name
    return content.ljust(row_length)


# def len_name(d):
#     return (len(d["name"]),
#         [len(s["name"]) for s in d["subcategories"])
# # """

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
