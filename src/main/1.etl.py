import pandas as pd

# Input
df = pd.read_csv("../../data/raw/Wholesale customers data.csv")
horeca_user_item_affinity = df[df["Channel"] == 1].reset_index().drop(["Channel", "Region", "index"], axis=1)
retail_user_item_affinity = df[df["Channel"] == 2].reset_index().drop(["Channel", "Region", "index"], axis=1)
del df

# Pearson correlation
horeca_item_similarity = horeca_user_item_affinity.corr()
retail_item_similarity = retail_user_item_affinity.corr()

# Add user column
horeca_user_item_affinity["customer_id"] = range(1, horeca_user_item_affinity.shape[0]+1)
retail_user_item_affinity["customer_id"] = range(1, retail_user_item_affinity.shape[0]+1)
horeca_user_item_affinity.columns = ["fresh", "milk", "grocery", "frozen", "detergents_paper", "delicassen", "customer_id"]
retail_user_item_affinity.columns = ["fresh", "milk", "grocery", "frozen", "detergents_paper", "delicassen", "customer_id"]
horeca_user_item_affinity = horeca_user_item_affinity[["customer_id", "fresh", "milk", "grocery", "frozen", "detergents_paper", "delicassen"]]
retail_user_item_affinity = retail_user_item_affinity[["customer_id", "fresh", "milk", "grocery", "frozen", "detergents_paper", "delicassen"]]

# Output
horeca_item_similarity.to_csv("../../data/interim/horeca_item_similarity.csv", index=False)
retail_item_similarity.to_csv("../../data/interim/retail_item_similarity.csv", index=False)
horeca_user_item_affinity.to_csv("../../data/interim/horeca_user_item_affinity.csv", index=False)
horeca_user_item_affinity.to_csv("../../data/interim/retail_user_item_affinity.csv", index=False)
