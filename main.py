from CollaborativeFiltering import CollaborativeFiltering

file_path = "21B_tag_views_dataset.csv"

cf = CollaborativeFiltering()

cf.load_data(file_path)

print("data loaded")

current_tag_id = "ff0d3fb21c00bc33f71187a2beec389e9eff5332"

similar_items = cf.similar_items(current_tag_id)

print("Users that viewed \"" + cf.products[current_tag_id] + "\" also viewed:")
print(similar_items)
