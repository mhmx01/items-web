function followUnfollow(event) {
    url = '/accounts/follow/';

    const followUnfollowButton = event.target;
    const action = followUnfollowButton.dataset.action;
    const username = followUnfollowButton.dataset.username;

    const followersCountSpan = document.querySelector('.followers-count');
    let followersCount = parseInt(followersCountSpan.textContent.trim());

    options = {
        method: 'POST',
        body: JSON.stringify({ action, username }),
        headers: {
            'content-type': 'application/json',
            'X-CSRFTOKEN': document.cookie.split(';').find(cookie => cookie.match(/^csrftoken=/)).replace('csrftoken=', ''),
        },
        mode: 'same-origin'
    };

    fetch(url, options)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        if (json.status === 'error') return;

        // const newAction = action === 'follow' ? 'unfollow' : 'follow';
        // action === 'follow' ? followersCount++ : followersCount--;
        let newAction;
        if (action === 'follow') {
            newAction = 'unfollow';
            followersCount++;
            followUnfollowButton.classList.replace('btn-success', 'btn-danger')
        } else {
            newAction = 'follow';
            followersCount--;
            followUnfollowButton.classList.replace('btn-danger', 'btn-success')
        }

        followUnfollowButton.dataset.action = newAction;
        followUnfollowButton.textContent = newAction;
        followersCountSpan.textContent = followersCount;
    })
    .catch(error => console.error(error.message));
}

const followUnfollowButton = document.querySelector('.follow');
if (followUnfollowButton) followUnfollowButton.addEventListener('click', followUnfollow)
