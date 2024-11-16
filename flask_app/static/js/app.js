document.getElementById("chat-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const chatLog = document.getElementById("chat-log");
    const userMessage = document.getElementById("user-message").value;

    // Display user's message
    chatLog.innerHTML += `<div class="chat-message user"><strong>User:</strong> ${userMessage}</div>`;
    document.getElementById("user-message").value = "";
    const loadingMessage = document.createElement("div");
    loadingMessage.classList.add("chat-message", "system", "loading-message");
    
    loadingMessage.innerHTML = `
        <strong>System:</strong>
        <div class="typing-dots">
            <span>.</span><span>.</span><span>.</span>
        </div>`;
    chatLog.appendChild(loadingMessage);
    chatLog.scrollTop = chatLog.scrollHeight;
    try {
        // Send message to backend
        const response = await fetch("/chat", {
            method: "POST",
            body: new URLSearchParams({ message: userMessage }),
        });

        const data = await response.json();
        const systemResponse = data.response;
        chatLog.removeChild(loadingMessage);

        // Display system's response
        chatLog.innerHTML += `<div class="chat-message system"><strong>System:</strong> ${systemResponse}</div>`;
        chatLog.scrollTop = chatLog.scrollHeight;
    } catch (error) {
        chatLog.removeChild(loadingMessage);
        chatLog.innerHTML += `<div class="chat-message system error"><strong>System:</strong> Oops, something went wrong!</div>`;
        console.error("Error sending message:", error);
    }
});
