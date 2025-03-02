const responses = {
    greeting: "Hello! How can I assist you today?",
    farewell: "Goodbye! Have a wonderful day!",
    // Add more responses as needed
};

function getResponse(intent) {
    return responses[intent] || "I'm sorry, I don't understand.";
}

// Read message from stdin
process.stdin.on('data', (data) => {
    const intent = data.toString().trim();
    const response = getResponse(intent);
    
    // Send response to stdout
    process.stdout.write(response + '\n');
});


