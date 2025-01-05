# Hierarchical tree for product categories
categories = {
    "Electronics": {"Phones", "Laptops"},
    "Home Appliances": {"Refrigerators", "Microwaves"}
}

for category, subcategories in categories.items():
    print(f"{category}: {', '.join(subcategories)}")
