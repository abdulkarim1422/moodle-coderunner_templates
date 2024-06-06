import subprocess, sys
SEPARATOR = "\n#<ab@17943918#@>#\n"
student_answer = """{{ STUDENT_ANSWER | e('py') }}"""
shell_list = []
def write_to(filename , content):
    with open(filename, 'a') as f:
        f.write(content)
def shell_add(x):
    for line in x.split("\n"):
        if (line):
            shell_list.append(line)
def shell_run(x, F):
    lines = []
    for line in x.split("\n"):
        if (line):
            lines.append(line)
    one_line = " && ".join(lines)
    try:
        result = subprocess.run(one_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        write_to(F, result.stdout)
    except subprocess.CalledProcessError as e:
        if e.stderr:
            write_to(F, e.stderr)
        if e.returncode < 0:
            write_to(F, f"Task failed with signal, {-e.returncode}")
        write_to(F, "ERROR")
# -------------- Don't edit before this -------------------------------------

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

# Edit after this --------------------------

file0 = "X.txt"
file1 = "X.txt"

prereq = """
mkdir folder0
cd folder0
"""

postreq = """
"""

shell_add(prereq)
shell_add(f"{student_answer} {postreq}")
one_line = " && ".join(shell_list)
shell_run(one_line, file0)

# --------------------------------------
{% for TEST in TESTCASES %}
testcode = """{{ TEST.testcode | e('py') }}"""
shell_run(testcode, file1)
{% if not loop.last %}
write_to(file1, SEPARATOR)
{% endif %}
{% endfor %}

with open(file1, "r") as f:
    print(f.read())
