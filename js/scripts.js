document.addEventListener("DOMContentLoaded", function() {
    const songList = document.getElementById('songs-list');

    fetch('/playlist/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok.');
            }
            return response.json();
        })
        .then(data => {
            songList.innerHTML = ''; // Clear the current list of songs
            data.songs.forEach(song => {
                const li = document.createElement('li');
                li.textContent = `${song.title} by ${song.artist}`;

                const playButton = document.createElement('a');
                playButton.textContent = 'Play on Spotify';
                playButton.href = song.url; // Link to Spotify
                playButton.target = '_blank'; // Open in new tab

                li.appendChild(playButton);
                songList.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Error fetching the songs:', error);
        });
});
