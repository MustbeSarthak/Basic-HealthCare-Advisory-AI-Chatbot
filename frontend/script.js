
const input = document.getElementById("message-input");
const sendButton = document.getElementById("send-btn");
const chatBox = document.getElementById("chat-box");


function addMessage(text, className) {

    const message = document.createElement("div");

    message.classList.add("message", className);

    message.textContent = text;

    chatBox.appendChild(message);

    // Scroll to latest message
    chatBox.scrollTop = chatBox.scrollHeight;
}


async function sendMessage() {

    const userMessage = input.value.trim();

    if (!userMessage) {
        return;
    }

    // Show user's message
    addMessage(userMessage, "user-message");

    // Clear input
    input.value = "";

    try {

        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: userMessage
            })
        });


        if (!response.ok) {
            throw new Error("Server error");
        }


        const data = await response.json();

        // Show AI response
        addMessage(data.response, "bot-message");


    } catch (error) {

        console.error(error);

        addMessage(
            "Bro, backend se connection nahi ho raha 😭",
            "bot-message"
        );
    }
}


// Send when button is clicked
sendButton.addEventListener("click", sendMessage);


// Send when Enter is pressed
input.addEventListener("keydown", function (event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});
