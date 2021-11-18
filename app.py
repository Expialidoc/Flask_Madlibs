from flask import Flask, request, render_template
from stories import Story
from flask_debugtoolbar import DebugToolbarExtension
# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )
# ans = {"place":'condo', "noun":'dragon', "verb":'fired', "adjective":'hot', "plural_noun":'love'}

story1 = Story(
    "history",
    "A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
story2 = Story(
    "predicament",
    "A Crooked Tale",
    ["noun", "adjective"],
    """There was a {adjective} man, and he went a {adjective} mile,
    He found a {adjective} {noun} against a {adjective} stile."""
)
# Make dict of {code:story, code:story, ...}
stories = {s.code: s for s in [story1, story2]}

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)
# @app.route('/madlib')
# def make_story():
#     s = story.generate(ans)
#     html = f'''<html><body><h1>{s}</h1></body></html>'''
#     return html
    
@app.route('/home')
def pick_story():
    
    return render_template('pick_story.html', stories=stories.values())

@app.route('/form')
def show_form():
    story_id = request.args["picks"]
    story = stories[story_id]
    prompts = story.prompts
    return render_template('form.html', story_id=story_id,title=story.title,prompts=prompts)

@app.route('/story')
def show_story():
    # place = request.args.get('place')
    # noun = request.args.get('noun')
    # verb = request.args.get('verb')
    # adjective = request.args.get('adjective')
    # plural_noun = request.args.get('plural_noun')
    # answer = {"place": place, "noun": noun, "verb": verb, "adjective": adjective, "plural_noun": plural_noun}
    answer = request.args
    story_id = request.args["picks"]
    story = stories[story_id]
    text = story.generate(answer)
    return render_template('story.html', title=story.title, text = text)