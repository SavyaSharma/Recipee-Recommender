source recipeeze/env/bin/activate
echo 'VENV activated'
export FLASK_APP=recipeeze
export FLASK_ENV=development
echo 'Dev environment set'
flask run
