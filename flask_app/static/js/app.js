document.getElementById("chat-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    
    const chatLog = document.getElementById("chat-log");
    const userMessage = document.getElementById("user-message").value;


    chatLog.innerHTML += `<div class="chat-message user"><strong>User:</strong> ${userMessage}</div>`;
    document.getElementById("user-message").value = "";
    
    const systemResponse="Hi whats your question?"
    chatLog.innerHTML += `
        
        <div class="chat-message system loading-message">
             <strong>System:</strong>
             <div class="typing-dots">
                <span>.</span>
                <span>.</span>
                <span>.</span>
                <span>.</span>
                <span>.</span>
                <span>.</span>
                
            </div>
        </div>`;
    
    chatLog.scrollTop = chatLog.scrollHeight;

    setTimeout(() => {
        const loadingMessage = chatLog.querySelector('.loading-message');
        if (loadingMessage) {
            loadingMessage.remove();
        }
        chatLog.innerHTML += `<div class="chat-message system"><strong>System:</strong> ${systemResponse}</div>`;
        chatLog.scrollTop = chatLog.scrollHeight;
    }, 3000);
        
   
});
