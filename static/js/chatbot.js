document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chatBox');
    const userInput = document.getElementById('userInput');
    const sendButton = document.getElementById('sendButton');
    
    function addMessage(message, isUser = true) {
        const msgDiv = document.createElement('div');
        msgDiv.className = isUser ? 'user-message' : 'bot-message';
        msgDiv.textContent = message;
        chatBox.appendChild(msgDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    sendButton.addEventListener('click', sendMessage);

    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;
        
        addMessage(message, true);
        userInput.value = '';
        
        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message })
            });
            
            const data = await response.json();
            addMessage(data.response, false);
        } catch (error) {
            addMessage('Error connecting to the chatbot', false);
        }
    }

    // Handle Enter key
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });
});