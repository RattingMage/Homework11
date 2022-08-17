from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route("/")
def home():
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:id>")
def info_candidate(id):
    candidate = get_candidate(id)
    return render_template('single.html', name=candidate["name"], position=candidate["position"], picture=candidate["picture"], skills=candidate["skills"])


@app.route("/skill/<skill_name>")
def skills_candidate(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template('skill.html', skill_name=skill_name, count=len(candidates), candidates=candidates)


@app.route("/search/<candidate_name>")
def name_candidate(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template('search.html', count=len(candidates), candidates=candidates)


app.run()
