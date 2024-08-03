def match_graduates_to_jobs(graduates, jobs):
    matches = []
    for grad in graduates:
        grad_skills = set(grad['skills'].split(','))
        for job in jobs:
            job_skills = set(job['required_skills'].split(','))
            if grad_skills.intersection(job_skills):
                matches.append((grad['id'], job['id']))
    return matches

# Example usage
graduates = [
    {'id': 1, 'skills': 'python, machine learning'},
    {'id': 2, 'skills': 'java, spring'}
]

jobs = [
    {'id': 1, 'required_skills': 'python, data science'},
    {'id': 2, 'required_skills': 'java, spring'}
]

matches = match_graduates_to_jobs(graduates, jobs)
print(matches)
