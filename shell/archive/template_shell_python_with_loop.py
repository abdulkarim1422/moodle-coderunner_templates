import subprocess, sys
SEPARATOR = "\n#<ab@17943918#@>#\n"
student_answer = """{{ STUDENT_ANSWER | e('py') }}"""
# -----------------

file0 = "X.txt"

prereq = """
mkdir folder0
cd folder0
"""

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


# -------------------------
def write_to(filename , content):
    with open(filename, 'a') as f:
        f.write(content)

def shell_run(x, F):
    lines = []
    for line in x.split("\n"):
        if (line):
            lines.append(line)
    one_line = " && ".join(lines)
    try:
        subprocess.run(f"{one_line} >> {F}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
    except subprocess.CalledProcessError as e:
        if e.stderr:
            write_to(F, e.stderr)
        if e.returncode < 0:
            write_to(F, f"Task failed with signal, {-e.returncode}")
        write_to(F, "ERROR")

# delete this if you don't have prerequired commands that will run before student code
shell_run(prereq, file0)

# edit this if you don't want the student code to show output (replace file0 with "bin")
shell_run(student_answer, file0)

{% for TEST in TESTCASES %}
testcode = """{{ TEST.testcode | e('py') }}"""
shell_run(testcode, file0)
{% if not loop.last %}
write_to(file0, SEPARATOR)
{% endif %}
{% endfor %}

with open(file0, "r") as f:
    print(f.read())
