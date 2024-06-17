/* Copyright © 2024 Walkline Wang (https://walkline.wang)
 * Gitee: https://gitee.com/walkline/code-completion-for-micropython
 */
import * as vscode from 'vscode';

let ext = vscode.extensions.getExtension("walklinewang.code-completion-for-micropython");

const config_name = "python";
const key_1 = "autoComplete.extraPaths";
const key_2 = "analysis.extraPaths";
const key_3 = "analysis.stubPath";
const value = `${ext?.extensionPath}\\code_completion`;

// https://blog.csdn.net/forward_huan/article/details/108084802
function update_configuration(cfgName: string, key: string, value: any,
	configurationTarget: vscode.ConfigurationTarget | boolean) {
	return new Promise((resolve, reject) => {
		let cfg = vscode.workspace.getConfiguration(cfgName);

		if (cfg.has(key)) {
			cfg.update(key, value, configurationTarget)
				.then(() => {
					vscode.window.showInformationMessage('Code completion setup successed');
					resolve(true);
				}).then(undefined, err => {
					vscode.window.showErrorMessage('Code completion setup failed');
					reject(err);
				});
		} else {
			resolve(false);
		}
	});
}

export function activate(context: vscode.ExtensionContext) {
	const setup = vscode.commands.registerCommand('extension.setup', () => {
		if (vscode.workspace.workspaceFolders?.length !== 0) {
			update_configuration(config_name, key_1, [value], vscode.ConfigurationTarget.Workspace);
			update_configuration(config_name, key_2, [value], vscode.ConfigurationTarget.Workspace);
			update_configuration(config_name, key_3, value, vscode.ConfigurationTarget.Workspace);

			// vscode.workspace.workspaceFolders?.forEach(folder => {
			// 	const workspace_root = folder.uri.fsPath;
			// 	const abconfig = vscode.Uri.file(`${workspace_root}\\abconfig`);

			// 	vscode.workspace.fs.stat(abconfig).then(
			// 		(onfulfilled) =>{
			// 			update_configuration(config_name, key_1, value, vscode.ConfigurationTarget.Workspace);
			// 			update_configuration(config_name, key_2, value, vscode.ConfigurationTarget.Workspace);
			// 		}
			// 	);
			// });
		}
	});

	const reset = vscode.commands.registerCommand('extension.reset', () => {
		if (vscode.workspace.workspaceFolders?.length !== 0) {
			update_configuration(config_name, key_1, [], vscode.ConfigurationTarget.Workspace);
			update_configuration(config_name, key_2, [], vscode.ConfigurationTarget.Workspace);
			update_configuration(config_name, key_3, "", vscode.ConfigurationTarget.Workspace);
		}
	});

	context.subscriptions.push(setup);
	context.subscriptions.push(reset);
}

export function deactivate() {}
