function registerUser() {
    const username = document.getElementById("reg-username").value.trim();
    const password = document.getElementById("reg-password").value.trim();

    if (username === "" || password === "") {
        alert("Please fill all fields!");
        return false;
    }

    // Store user in localStorage
    if (localStorage.getItem(username)) {
        alert("User already exists!");
        return false;
    }

    localStorage.setItem(username, password);
    alert("Registration successful! Please login.");
    window.location.href = "index.html";
    return false;
}

function loginUser() {
    const username = document.getElementById("login-username").value.trim();
    const password = document.getElementById("login-password").value.trim();

    const storedPassword = localStorage.getItem(username);

    if (storedPassword && storedPassword === password) {
        alert(`Welcome ${username}!`);
    } else {
        alert("Invalid credentials!");
    }

    return false;
}
