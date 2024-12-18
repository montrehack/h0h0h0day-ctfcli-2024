function sd(value) {
    return String(value.toFixed(2)).padStart(5, '0');
}


(function () {
    'use strict';

    // Does the browser actually support the video element?
    var supportsVideo = !!document.createElement('video').canPlayType;

    if (!supportsVideo) {
        return;
    }

    const videoContainer = document.getElementById('video-container');
    const video = document.getElementById('video');
    const videoControls = document.getElementById('video-controls');

    video.controls = false;

    // Display the user defined video controls
    videoControls.setAttribute('data-state', 'visible');

    // Obtain handles to buttons and other elements
    const playpause = document.getElementById('playpause');
    const stop = document.getElementById('stop');
    const mute = document.getElementById('mute');
    const volinc = document.getElementById('volinc');
    const voldec = document.getElementById('voldec');
    const seek = document.getElementById('seek');

    // labels
    const timeLabel = document.getElementById('time-label');
    const volumeLabel = document.getElementById('volume-label');
    const mutedLabel = document.getElementById('muted-label');

    // Check the volume
    var checkVolume = function (dir) {
        if (dir) {
            var currentVolume = Math.floor(video.volume * 10) / 10;
            if (dir === '+') {
                if (currentVolume < 1) video.volume += 0.1;
            }
            else if (dir === '-') {
                if (currentVolume > 0) video.volume -= 0.1;
            }
            // If the volume has been turned off, also set it as muted
            // Note: can only do this with the custom control set as when the 'volumechange' event is raised, there is no way to know if it was via a volume or a mute change
            if (currentVolume <= 0) video.muted = true;
            else video.muted = false;

            volumeLabel.innerText = "Volume: " +  Math.floor(video.volume * 100) + "%";
            mutedLabel.innerText = video.muted ? "Muted" : "";
        }
        changeButtonState('mute');
    }

    // Change the volume
    var alterVolume = function (dir) {
        checkVolume(dir);
    }

    if (document.addEventListener) {
        // Wait for the video's meta data to be loaded, then set the progress bar's max value to the duration of the video
        video.addEventListener('loadedmetadata', function () {
            seek.setAttribute('max', video.duration * 100);
            mutedLabel.innerText = video.muted ? "Muted" : "NotMuted";
            volumeLabel.innerText = "Volume: " +  Math.floor(video.volume * 100) + "%";
            timeLabel.innerText =  `${sd(video.currentTime)} / ${sd(video.duration)}`;   
        });

        // Changes the button state of certain button's so the correct visuals can be displayed with CSS
        var changeButtonState = function (type) {
            // Play/Pause button
            if (type == 'playpause') {
                if (video.paused || video.ended) {
                    playpause.setAttribute('data-state', 'play');
                }
                else {
                    playpause.setAttribute('data-state', 'pause');
                }
            }
            // Mute button
            else if (type == 'mute') {
                mute.setAttribute('data-state', video.muted ? 'unmute' : 'mute');
                mutedLabel.innerText = video.muted ? "Muted" : "";
            }
        }

        // Add event listeners for video specific events
        video.addEventListener('play', function () {
            changeButtonState('playpause');
        }, false);
        video.addEventListener('pause', function () {
            changeButtonState('playpause');
        }, false);
        video.addEventListener('volumechange', function () {
            checkVolume();
        }, false);

        // Add events for all buttons			
        playpause.addEventListener('click', function (e) {
            
            if (video.paused || video.ended) video.play();
            else video.pause();
        });

        // The Media API has no 'stop()' function, so pause the video and reset its time and the progress bar
        stop.addEventListener('click', function (e) {
            video.pause();
            video.currentTime = 0;
            seek.value = 0;
            // Update the play/pause button's 'data-state' which allows the correct button image to be set via CSS
            changeButtonState('playpause');
        });
        mute.addEventListener('click', function (e) {
            video.muted = !video.muted;
            changeButtonState('mute');
        });
        volinc.addEventListener('click', function (e) {
            alterVolume('+');
        });
        voldec.addEventListener('click', function (e) {
            alterVolume('-');
        });

        // As the video is playing, update the progress bar
        video.addEventListener('timeupdate', function () {
            if (video.getAttribute('data-state') === 'house' && (video.currentTime > 6 && video.currentTime < 10)) {
                video.currentTime = 10;
            }
            if (!seek.getAttribute('max')) seek.setAttribute('max', Math.floor(video.duration * 100));
            seek.value = Math.floor(video.currentTime * 100);
            timeLabel.innerText =  `${sd(video.currentTime)} / ${sd(video.duration)}`;        
        });

        seek.addEventListener('input', function () {
            const next_value = this.value / 100;
            if (video.getAttribute('data-state') !== 'house' || !(next_value > 6 && next_value < 10)) {
                video.currentTime = this.value / 100;
            }
        });
    }
})();