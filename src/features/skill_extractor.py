import re

SKILLS=[

"python",
"java",
"c++",
"sql",
"power bi",
"excel",
"tableau",
"machine learning",
"deep learning",
"tensorflow",
"pytorch",
"aws",
"azure",
"docker",
"kubernetes",
"flask",
"django",
"react",
"nodejs",
"git",
"linux",
"mongodb",
"mysql",
"pandas",
"numpy",
"opencv",
"nlp",
"spark",
"hadoop"

]


def extract_skills(text):

    text=text.lower()

    found=[]

    for skill in SKILLS:

        if re.search(r"\b"+re.escape(skill)+r"\b",text):

            found.append(skill)

    return sorted(set(found))