document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registration-form');

    if (form) {
        form.addEventListener('submit', async function (e) {
            e.preventDefault();

            const username = document.querySelector('input[name="username"]').value;
            const email = document.querySelector('input[name="email"]').value;
            const password = document.querySelector('input[name="password"]').value;

            if (!username || !email || !password) {
                alert('Please fill in all fields.');
                return;
            }

            try {
                const response = await fetch('/api/user/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        username: username,
                        email: email,
                        password: password,
                    }),
                });

                const data = await response.json();

                if (response.ok) {
                    alert(data.message);
                    window.location.href = '/';
                } else {
                    alert('Error: ' + data.message);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Something went wrong! Please try again.');
            }
        });
    } else {
        console.error('Form not found!');
    }
});


document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('login-form');

    if (form) {
        form.addEventListener('submit', async function (e) {
            e.preventDefault();

            const username = document.querySelector('input[name="username"]').value;
            const password = document.querySelector('input[name="password"]').value;

            try {
                const response = await fetch('/api/user/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        username: username,
                        password: password,
                    }),
                });

                const data = await response.json();

                if (response.ok) {
                    window.location.href = '/dashboard';
                } else {
                    alert('Error: ' + data.message);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Something went wrong! Please try again.');
            }
        });
    } else {
        console.error('Form not found!');
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('update-form');

    if (form) {
        form.addEventListener('submit', async function (e) {
            e.preventDefault();

            const email = document.querySelector('input[name="email"]').value;
            const address = document.querySelector('input[name="address"]').value;
            const phone = document.querySelector('input[name="phone"]').value;
            const new_pass = document.querySelector('input[name="password"]').value;

            try {
                const response = await fetch('/api/user/update', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        email: email,
                        address: address,
                        phone: phone,
                        password: new_pass
                    }),
                });

                const data = await response.json();

                if (response.ok) {
                    alert(data.message);
                } else {
                    alert('Error: ' + data.message);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Something went wrong! Please try again.');
            }
        });
    } else {
        console.error('Form not found!');
    }
});
