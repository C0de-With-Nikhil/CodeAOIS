const vscode = require('vscode');
const { exec } = require('child_process');

function activate(context) {
    let disposable = vscode.commands.registerCommand('codeaois.startChat', () => {
        // Create the Webview Panel
        const panel = vscode.window.createWebviewPanel(
            'codeAoisChat',
            'CodeAOIS AI Developer',
            vscode.ViewColumn.Two, // Opens on the side
            { enableScripts: true }
        );

        // Define the HTML UI
        panel.webview.html = getWebviewContent();

        // Handle messages sent from the UI
        panel.webview.onDidReceiveMessage(
            message => {
                if (message.command === 'sendTask') {
                    // Send message back to UI that we are thinking
                    panel.webview.postMessage({ command: 'receiveMessage', text: '🤖 *CodeAOIS team is working...*' });

                    // BULLETPROOF FIX: Hardcode the absolute path to your CodeAOIS backend
                    // This guarantees it finds your virtual environment no matter what folder is open
                    const codeAoisPath = '/home/nikhil/codeaois';
                    const pythonPath = '/home/nikhil/codeaois/aois_env/bin/python';
                    
                    const commandToRun = `"${pythonPath}" -m cli.main "${message.text}"`;

                    // Execute the Python backend using the exact CodeAOIS directory
                    exec(commandToRun, { cwd: codeAoisPath }, (err, stdout, stderr) => {
                        let response = stdout;
                        if (err) response = `Error: ${err.message}`;
                        
                        // Ignore minor git branch warnings if they happen, but capture real errors
                        if (stderr && !stderr.includes("already exists")) {
                            response += `\nStderr: ${stderr}`;
                        }
                        
                        // Send the result back to the chat UI
                        panel.webview.postMessage({ command: 'receiveMessage', text: response });
                    });
                }
            },
            undefined,
            context.subscriptions
        );
    });

    context.subscriptions.push(disposable);
}

// Simple HTML/CSS/JS for the Chat Interface
function getWebviewContent() {
    return `<!DOCTYPE html>
    <html lang="en">
    <head>
        <style>
            body { font-family: sans-serif; padding: 10px; display: flex; flex-direction: column; height: 95vh; }
            #chat-box { flex-grow: 1; overflow-y: auto; margin-bottom: 10px; border: 1px solid #444; padding: 10px; background: #1e1e1e; color: #d4d4d4; white-space: pre-wrap;}
            #input-box { display: flex; }
            #task-input { flex-grow: 1; padding: 8px; background: #3c3c3c; color: white; border: 1px solid #555; }
            button { padding: 8px 15px; background: #007acc; color: white; border: none; cursor: pointer; }
            button:hover { background: #005999; }
        </style>
    </head>
    <body>
        <h2>CodeAOIS Team</h2>
        <div id="chat-box"></div>
        <div id="input-box">
            <input type="text" id="task-input" placeholder="Ask CodeAOIS to build something..." />
            <button onclick="sendTask()">Send</button>
        </div>
        <script>
            const vscode = acquireVsCodeApi();
            const chatBox = document.getElementById('chat-box');
            const taskInput = document.getElementById('task-input');

            // Handle incoming messages from the extension
            window.addEventListener('message', event => {
                const message = event.data;
                if (message.command === 'receiveMessage') {
                    chatBox.innerHTML += '<div><b>CodeAOIS:</b><br>' + message.text + '</div><hr>';
                    chatBox.scrollTop = chatBox.scrollHeight;
                }
            });

            // Send task to the extension
            function sendTask() {
                const text = taskInput.value;
                if (!text) return;
                chatBox.innerHTML += '<div><b>You:</b> ' + text + '</div><br>';
                vscode.postMessage({ command: 'sendTask', text: text });
                taskInput.value = '';
            }

            // Allow pressing Enter to send
            taskInput.addEventListener('keypress', function (e) {
                if (e.key === 'Enter') sendTask();
            });
        </script>
    </body>
    </html>`;
}

function deactivate() {}
module.exports = { activate, deactivate };