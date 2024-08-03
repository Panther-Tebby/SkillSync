import requests
from bs4 import BeautifulSoup

# Example function to scrape job data (replace with actual URLs and parsing logic)
def scrape_job_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    jobs = []
    for job in soup.find_all('div', class_='job'):
        title = job.find('h2').text
        skills = job.find('p', class_='skills').text
        jobs.append({'title': title, 'skills': skills})
    
    return jobs

# Example usage
job_data = scrape_job_data('https://example.com/jobs')
