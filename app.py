import os
from zipfile import ZipFile

# File structure and content
files = {
    "mongodb-ecommerce-demo/README.md": "#  MongoDB E-Commerce Demo\n\nThis project provides a sample MongoDB dataset...",
    "mongodb-ecommerce-demo/data/customers.json": "[\n  {\n    \"_id\": { \"$oid\": \"64a1c1e1f0f1a1a1a1a1a101\" },\n    \"name\": \"Alice Smith\",\n    ...\n  }\n]",
    "mongodb-ecommerce-demo/data/products.json": "[\n  {\n    \"_id\": { \"$oid\": \"64a1c1e1f0f1a1a1a1a1b201\" },\n    \"name\": \"Wireless Mouse\",\n    ...\n  }\n]",
    "mongodb-ecommerce-demo/data/orders.json": "[\n  {\n    \"_id\": { \"$oid\": \"64a1c1e1f0f1a1a1a1a1c301\" },\n    \"customer_id\": { \"$oid\": \"64a1c1e1f0f1a1a1a1a1a101\" },\n    ...\n  }\n]",
    "mongodb-ecommerce-demo/queries/advanced_queries.js": "// 1. Join orders with customers\ndb.orders.aggregate([\n  {\n    $lookup: {\n      from: \"customers\",\n      localField: \"customer_id\",\n      foreignField: \"_id\",\n      as: \"customer_info\"\n    }\n  },\n  ...\n]);"
}

# Create folders and write files
for path, content in files.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# Create the zip archive
with ZipFile("mongodb-ecommerce-demo.zip", "w") as zipf:
    for path in files:
        zipf.write(path)

# Optional: Clean up temporary folders/files after zipping
# for path in files:
#     os.remove(path)
