{{ STUDENT_ANSWER }}

var SEPARATOR = "#<ab@17943918#@>#";

{% for TEST in TESTCASES %}
{{ TEST.testcode }}
{% if not loop.last %}
console.log(SEPARATOR);
{% endif %}
{% endfor %}

let __student_answer__ = "{{ STUDENT_ANSWER | e('js') }}"

let all_white_police = ["word1", "word2", "word3"];
if (!all_white_police.every(x => __student_answer__.includes(x))) 
{console.log("شرطة إبتكار");}

let any_white_police = ["word1", "word2", "word3"];
if (!any_white_police.some(x => __student_answer__.includes(x)))
{console.log("شرطة إبتكار");}

let dark_police = ["word1", "word2", "word3"];
if (dark_police.some(x => __student_answer__.includes(x))) 
{console.log("شرطة إبتكار");}


// __student_answer__.toLowerCase()
