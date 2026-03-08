const vscode = require('vscode');
const { exec } = require('child_process');

function activate(context) {
    let disposable = vscode.commands.registerCommand('codeaois.runTask', async () => {
        const task = await vscode.window.showInputBox({ prompt: 'Enter CodeAOIS task:' });
        if (task) {
            exec(`python -m cli.main task "${task}"`, (err, stdout, stderr) => {
                if (err) vscode.window.showErrorMessage(err.message);
                else vscode.window.showInformationMessage(stdout);
            });
        }
    });
    context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = { activate, deactivate };