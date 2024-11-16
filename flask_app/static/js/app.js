document.getElementById("chat-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const chatLog = document.getElementById("chat-log");
    const userMessage = document.getElementById("user-message").value;

    // Display user's message
    chatLog.innerHTML += `<div class="chat-message user"><strong>User:</strong> ${userMessage}</div>`;
    document.getElementById("user-message").value = "";

    try {
        // Send message to backend
        const response = await fetch("/chat", {
            method: "POST",
            body: new URLSearchParams({ message: userMessage }),
        });

        const data = await response.json();
        const systemResponse = data.response;

        // Display system's response
        chatLog.innerHTML += `<div class="chat-message system"><strong>System:</strong> ${systemResponse}</div>`;
        chatLog.scrollTop = chatLog.scrollHeight;
    } catch (error) {
        console.error("Error sending message:", error);
    }
});
