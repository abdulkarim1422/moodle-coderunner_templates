__student_answer__ = """{{ STUDENT_ANSWER | e('py') }}"""

import subprocess, sys

{% for TEST in TESTCASES %}

testcode = """{{ TEST.testcode | e('py') }}"""

template = """
var SEPARATOR = "#<ab@17943918#@>#";

%s

%s

{% if not loop.last %} console.log(SEPARATOR); {% endif %}
"""

with open("0.js", 'w') as js_file:
    js_file.write(template % (__student_answer__, testcode)) 

subprocess.run("node './0.js'", shell=True)

{% endfor %}


# POLICE
black_police = ["word0", "word1", "word2"]
if any(x in student_answer for x in black_police) :
    print("شرطة إبتكار")

all_white_police = ["word0", "word1", "word2"]
if any(x not in student_answer for x in all_white_police) :
    print("شرطة إبتكار")

any_white_police = ["word0", "word1", "word2"]
if all(x in student_answer for x in any_white_police) :
    print("شرطة إبتكار")