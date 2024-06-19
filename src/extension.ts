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
					resolve(true);
				})
				.then(undefined, error => {
					reject(error);
				});
		} else {resolve(false);}
	});
}

export function activate(context: vscode.ExtensionContext) {
	const enable = vscode.commands.registerCommand('extension.enable', () => {
		update_configuration(config_name, key_1, [value], vscode.ConfigurationTarget.Workspace)
		.then((resolved) => {
			if (resolved) {
				update_configuration(config_name, key_2, [value], vscode.ConfigurationTarget.Workspace)
				.then((resolved) => {
					if (resolved) {
						update_configuration(config_name, key_3, value, vscode.ConfigurationTarget.Workspace)
						.then(() => {
							vscode.window.showInformationMessage('Update settings successed.');
						});
					}
				});
			} else {
				vscode.window.showErrorMessage(`Update settings failed: Configuration key '${config_name}' not found.`, 'OK');
			}
		}).catch((error) => {
			vscode.window.showErrorMessage(`Update settings failed: ${error.message}`, 'OK');
		});
	});

	const disable = vscode.commands.registerCommand('extension.disable', () => {
		update_configuration(config_name, key_1, [], vscode.ConfigurationTarget.Workspace)
		.then((resolved) => {
			if (resolved) {
				update_configuration(config_name, key_2, [], vscode.ConfigurationTarget.Workspace)
				.then((resolved) => {
					if (resolved) {
						update_configuration(config_name, key_3, "", vscode.ConfigurationTarget.Workspace)
						.then(() => {
							vscode.window.showInformationMessage('Update settings successed.');
						});
					}
				});
			} else {
				vscode.window.showErrorMessage(`Update settings failed: Configuration '${config_name}' not found.`, 'OK');
			}
		}).catch((error) => {
			vscode.window.showErrorMessage(`Update settings failed: ${error.message}`, 'OK');
		});
	});

	context.subscriptions.push(enable, disable);
}

export function deactivate() {}
