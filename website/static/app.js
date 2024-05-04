let intro = document.querySelector('.intro');
let logo = document.querySelector('.logo-header');
let logoSpan = document.querySelectorAll('.intro-logo');

window.addEventListener('DOMContentLoaded', ()=>{
    setTimeout(()=>{

        logoSpan.forEach((span, idx)=>{
            setTimeout(()=>{
                span.classList.add('active');
            }, (idx + 1) * 400)
        });

        setTimeout(()=>{
            logoSpan.forEach((span, idx)=>{
                setTimeout(()=>{
                    span.classList.remove('active');
                    span.classList.add('fade');
                }, (idx + 1) * 50)
            })
        }, 2000);

        setTimeout(()=>{
            intro.style.top = '-100vh'
        }, 2300)
    })
})


document.addEventListener("DOMContentLoaded", function() {
    const synonymButton = document.querySelector('.synonym-button');
    const entryBox = document.querySelector('.entry-box');
    const synonymList = document.getElementById('synonymList');

    synonymButton.addEventListener('click', function() {
        const word = entryBox.value;
        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({word: word})
        })
        .then(response => response.json())
        .then(data => {
            synonymList.innerHTML = ''; // Clear previous results

            // Check if data is not empty
            if (data.length === 0) {
                synonymList.innerHTML = 'No synonyms found.';
                return;
            }

            // Create and append elements for each entry
            data.forEach(entry => {
                const entryDiv = document.createElement('div');
                entryDiv.className = 'entry';

                // Part of speech
                const pos = document.createElement('h4');
                pos.textContent = `Part of Speech: ${entry.part_of_speech}`;
                entryDiv.appendChild(pos);

                // Synonyms
                if (entry.synonyms.length > 0) {
                    const syns = document.createElement('p');
                    syns.innerHTML = `<strong>Synonyms:</strong> ${entry.synonyms.join(', ')}`;
                    entryDiv.appendChild(syns);
                }

                // Antonyms
                if (entry.antonyms.length > 0) {
                    const ants = document.createElement('p');
                    ants.innerHTML = `<strong>Antonyms:</strong> ${entry.antonyms.join(', ')}`;
                    entryDiv.appendChild(ants);
                }

                // Definitions
                if (entry.definitions.length > 0) {
                    const defs = document.createElement('p');
                    defs.innerHTML = `<strong>Definitions:</strong> ${entry.definitions.join('; ')}`;
                    entryDiv.appendChild(defs);
                }

                synonymList.appendChild(entryDiv);
            });
        })
        .catch(error => {
            console.error('Error:', error);
            synonymList.innerHTML = 'Error loading synonyms.';
        });
    });
});
