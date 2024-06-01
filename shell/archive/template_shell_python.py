import subprocess, sys
SEPARATOR = "\n#<ab@17943918#@>#\n"

file0 = "X.txt"

def write_to(filename , content):
    with open(filename, 'a') as f:
        f.write(content)

def shell_run(x, F):
    for line in x.split("\n"):
        if (line):
            try:
                subprocess.run(f"{line} >> {F}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
            except subprocess.CalledProcessError as e:
                if e.stderr:
                    write_to(F, e.stderr)
                if e.returncode < 0:
                    write_to(F, f"Task failed with signal, {-e.returncode}")
                write_to(F, "ERROR")

student_answer = """{{ STUDENT_ANSWER | e('py') }}"""

shell_run(student_answer, file0)


{% for TEST in TESTCASES %}

testcode = """{{ TEST.testcode | e('py') }}"""

shell_run(testcode, file0)

{% if not loop.last %}
write_to(file0, SEPARATOR)
{% endif %}

{% endfor %}


black_police = ["word0", "word1", "word2"]
if any(x in student_answer for x in black_police) :
    print("شرطة إبتكار")


all_white_police = ["word0", "word1", "word2"]
if any(x not in student_answer for x in all_white_police) :
    print("شرطة إبتكار")


any_white_police = ["word0", "word1", "word2"]
if all(x in student_answer for x in any_white_police) :
    print("شرطة إبتكار")


with open(file0, "r") as x_file:
    x_content = x_file.read()
    print(x_content)
