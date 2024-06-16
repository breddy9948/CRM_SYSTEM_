// script.js

document.getElementById('customerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value
    };
    
    fetch('/customers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        // Optionally, update UI or redirect to another page
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('interactionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = {
        customer_id: document.getElementById('customerId').value,
        type: document.getElementById('type').value,
        details: document.getElementById('details').value
    };
    
    fetch('/interactions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        // Optionally, update UI or redirect to another page
    })
    .catch(error => console.error('Error:', error));
});
