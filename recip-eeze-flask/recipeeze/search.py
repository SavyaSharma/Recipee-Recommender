import pandas as pd
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from recipeeze.auth import login_required
from recipeeze.db import get_db
from recipeeze import rr_main

bp = Blueprint('search', __name__)

@bp.route('/')
def index():
    #get the ingredients and search
    return render_template('search/index.html')#, posts=posts)

@bp.route('/recipe', methods=['POST'])
#@login_required
def recipe():
    #posting the results
    user_id = g.user['username']
    ingredient_list = request.form['ingredients']
    recipe_list = rr_main.set_up_rr(user_id,ingredient_list)
    recipe_list = recipe_list.to_numpy()
    recipe_table = pd.DataFrame(rr_main.mk_tbl(recipe_list))
    num_ = int(recipe_table.shape[0])
    return render_template('search/recipe.html',recipe_table = recipe_table,num_=num_)
