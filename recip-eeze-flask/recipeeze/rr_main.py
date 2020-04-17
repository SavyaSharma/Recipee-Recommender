#recipe recommender
import pandas as pd
import numpy as np
import heapq
import pickle
import os

filename = 'recipeeze/model/recipes_recommender_model.sav'
item_based_recommender = pickle.load(open(filename, 'rb'))

recipes_df = pd.read_csv('recipeeze/datasets/rr-recipes.csv')
users_df = pd.read_csv('recipeeze/datasets/rr-users.csv')
ratings_df = pd.read_csv('recipeeze/datasets/rr-ratings.csv')

def mk_tbl(rows):
    #this is for creating dynamic tables
    arr = []
    for row in rows:
        title = row[2]
        r_t = row[5]
        p_t = row[3]
        c_t = row[4]
        url = row[8]
        pred = row[9]
        arr.append([pred,title,r_t,p_t,c_t,url])
    return arr

def get_r(user_id):
    # Select which system to use. Due to memory constraints, item based is the only viable option
    recommender_system = item_based_recommender
    # N will represent how many items to recommend
    N = 2000

    # The setting to a set and back to list is a failsafe.
    rated_items = list(set(ratings_df.loc[ratings_df['user'] == user_id]['item'].tolist()))
    ratings_list = recipes_df['recipe_id'].values.tolist()
    reduced_ratings = ratings_df.loc[ratings_df['item'].isin(ratings_list)].copy()

    # Self explanitory name
    all_item_ids = list(set(reduced_ratings['item'].tolist()))

    # New_items just represents all the items not rated by the user
    new_items = [x for x in all_item_ids if x not in rated_items]

    # Estimate ratings for all unrated items
    predicted_ratings = {}
    for item_id in new_items:
        predicted_ratings[item_id] = recommender_system.predict(user_id, item_id).est
        pass

    # Get the item_ids for the top ratings
    recommended_ids = heapq.nlargest(N, predicted_ratings, key=predicted_ratings.get)
    recommended_ids = sorted(recommended_ids)

    # predicted_ratings
    recommended_df = recipes_df.loc[recipes_df['recipe_id'].isin(recommended_ids)].copy()
    #recommended_df.insert(1, 'pred_rating', np.zeros(len(recommended_ids)))
    recommended_df.insert(1, 'pred_rating', 0)

    # recommended_df = recipes_df.copy()
    for idx,item_id in enumerate(recommended_ids):
        recommended_df.iloc[idx, recommended_df.columns.get_loc('pred_rating')] = int(predicted_ratings[item_id])
        pass
    return recommended_df.head(N).sort_values('pred_rating', ascending=False)

def reg_frame(f_list,items):
    s_ = ''
    for i in items:
        str_ = f'(?=.*{i})'
        s_ += str_
    s_
    f_list = f_list[f_list['ingredients'].str.contains(fr'^\b{s_}\b',regex=True)]
    return f_list

def set_up_rr(user_id,i_list):
    f_list = get_r(user_id)
    items = i_list.split(',')
    f_list = reg_frame(f_list,items)
    f_list = f_list.reset_index(drop=True)
    f_list = f_list.T.reset_index(drop=True).T
    #f_list = f_list.head(10)
    return f_list
