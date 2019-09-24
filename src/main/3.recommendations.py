import pandas as pd
import numpy as np
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# Input
horeca_item_similarity = pd.read_csv("../../data/interim/horeca_item_similarity.csv")
retail_item_similarity = pd.read_csv("../../data/interim/retail_item_similarity.csv")
horeca_user_item_affinity = pd.read_csv("../../data/interim/horeca_user_item_affinity.csv")
retail_user_item_affinity = pd.read_csv("../../data/interim/retail_user_item_affinity.csv")
horeca_user_item_affinity = horeca_user_item_affinity.set_index("customer_id").T
retail_user_item_affinity = retail_user_item_affinity.set_index("customer_id").T

# Recommendation scores
horeca_recommendation_scores = pd.DataFrame(np.matmul(horeca_item_similarity, horeca_user_item_affinity))
retail_recommendation_scores = pd.DataFrame(np.matmul(retail_item_similarity, retail_user_item_affinity))
horeca_recommendation_scores.columns = range(1, horeca_recommendation_scores.shape[1]+1)
retail_recommendation_scores.columns = range(1, retail_recommendation_scores.shape[1]+1)

# Normalize
normalized_horeca_recommendation_scores = pd.DataFrame()
normalized_retail_recommendation_scores = pd.DataFrame()
for column in horeca_recommendation_scores.columns:
    normalized_horeca_recommendation_scores[column] = horeca_recommendation_scores[column] * (horeca_user_item_affinity[column].max() / horeca_recommendation_scores[column].max())
for column in retail_recommendation_scores.columns:
    normalized_retail_recommendation_scores[column] = retail_recommendation_scores[column] * (retail_user_item_affinity[column].max() / retail_recommendation_scores[column].max())

# Difference
differenced_horeca_recommendations = np.subtract(normalized_horeca_recommendation_scores, horeca_user_item_affinity)
differenced_retail_recommendations = np.subtract(normalized_retail_recommendation_scores, retail_user_item_affinity)
differenced_horeca_recommendations["category"] = ["fresh", "milk", "grocery", "frozen", "detergents_paper", "delicassen"]
differenced_retail_recommendations["category"] = ["fresh", "milk", "grocery", "frozen", "detergents_paper", "delicassen"]
differenced_horeca_recommendations = differenced_horeca_recommendations.set_index("category").reset_index()
differenced_retail_recommendations = differenced_retail_recommendations.set_index("category").reset_index()

# Final recommendations
final_horeca_recommendations = differenced_horeca_recommendations.\
                                  melt(id_vars=["category"],
                                       var_name="customer",
                                       value_name="score").\
                                   sort_values(by="score", ascending=False)
final_retail_recommendations = differenced_retail_recommendations.\
                                  melt(id_vars=["category"],
                                       var_name="customer",
                                       value_name="score").\
                                   sort_values(by="score", ascending=False)

final_horeca_recommendations.to_csv("../../data/processed/final_horeca_recommendations.csv", index=False)
final_retail_recommendations.to_csv("../../data/processed/final_retail_recommendations.csv", index=False)
