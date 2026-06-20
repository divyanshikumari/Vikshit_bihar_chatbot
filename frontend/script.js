// Fill input from sample question click
function fillInput(el) {
    document.getElementById('userInput').value = el.textContent;
    document.getElementById('userInput').focus();
}

// Enter key to send message
document.getElementById('userInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Send message
function sendMessage() {

    const input = document.getElementById('userInput');
    const text = input.value.trim();

    if (!text) return;

    const chat = document.getElementById('chatMessages');

    // User message
    const userMsg = document.createElement('div');
    userMsg.className = 'msg user';
    userMsg.innerHTML = `
        <div class="msg-avatar">👤</div>
        <div class="msg-bubble">${text}</div>
    `;

    chat.appendChild(userMsg);
    input.value = "";

    // Typing indicator
    const typing = document.createElement('div');
    typing.className = 'msg bot';
    typing.id = 'typing';
    typing.innerHTML = `
        <div class="msg-avatar">AI</div>
        <div class="msg-bubble">
            ⏳ Searching for answer...
        </div>
    `;

    chat.appendChild(typing);
    chat.scrollTop = chat.scrollHeight;

    // API Call
    fetch('http://127.0.0.1:8000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            question: text
        })
    })
    .then(response => response.json())
    .then(data => {
        typing.remove();
        if (data.answer) {
            addBotMessage(data.answer);
        } else {
            addBotMessage("No answer found. Please try again.");
        }
    })
    .catch(error => {
        console.error(error);
        typing.remove();
        addBotMessage("❌ Could not connect to server. Please check the backend.");
    });
}

// Add bot message
function addBotMessage(text) {
    const chat = document.getElementById('chatMessages');
    const botMsg = document.createElement('div');
    botMsg.className = 'msg bot';
    botMsg.innerHTML = `
        <div class="msg-avatar">AI</div>
        <div class="msg-bubble">${text}</div>
    `;
    chat.appendChild(botMsg);
    chat.scrollTop = chat.scrollHeight;
}