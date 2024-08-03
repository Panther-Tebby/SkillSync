document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript is working!");

    // Form validation and AJAX request
    const form = document.getElementById('skillsForm');
    const skillsInput = document.getElementById('skills');
    const skillsError = document.getElementById('skillsError');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const resultsDiv = document.getElementById('results');
    const matchesList = document.getElementById('matchesList');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        const skills = skillsInput.value.trim();
        
        if (skills === '') {
            skillsError.textContent = 'Please enter your skills.';
        } else {
            skillsError.textContent = '';
            loadingIndicator.style.display = 'block';
            resultsDiv.style.display = 'none';
            matchesList.innerHTML = ''; // Clear previous results

            // Simulate loading delay for demo purposes
            setTimeout(function() {
                fetch('/match', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ skills: skills })
                })
                .then(response => response.json())
                .then(data => {
                    loadingIndicator.style.display = 'none';
                    resultsDiv.style.display = 'block';
                    if (data.matches.length === 0) {
                        matchesList.innerHTML = '<li>No matching jobs found.</li>';
                    } else {
                        data.matches.forEach(match => {
                            const li = document.createElement('li');
                            li.textContent = `${match.title} at ${match.company} (Skills required: ${match.required_skills})`;
                            matchesList.appendChild(li);
                        });
                    }
                })
                .catch(error => {
                    loadingIndicator.style.display = 'none';
                    console.error('Error fetching matches:', error);
                });
            }, 1000); // Adjust delay as needed
        }
    });

});


