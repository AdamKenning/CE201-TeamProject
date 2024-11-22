
// Get references to the tabs and forms
const loginTab = document.getElementById('login-tab');
const registerTab = document.getElementById('register-tab');
const loginForm = document.getElementById('login-form');
const registerForm = document.getElementById('register-form');

// Add event listener for Login tab
loginTab.addEventListener('click', () => {
  loginTab.classList.add('active'); // Highlight the Login tab
  registerTab.classList.remove('active'); // Remove highlight from Register tab
  loginForm.classList.add('active'); // Show the Login form
  registerForm.classList.remove('active'); // Hide the Register form
});

// Add event listener for Register tab
registerTab.addEventListener('click', () => {
  registerTab.classList.add('active'); // Highlight the Register tab
  loginTab.classList.remove('active'); // Remove highlight from Login tab
  registerForm.classList.add('active'); // Show the Register form
  loginForm.classList.remove('active'); // Hide the Login form
});