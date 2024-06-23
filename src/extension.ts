/* Copyright © 2024 Walkline Wang (https://walkline.wang)
 * Gitee: https://gitee.com/walkline/code-completion-for-micropython
 */
import * as vscode from 'vscode';

let ext = vscode.extensions.getExtension("walklinewang.code-completion-for-micropython");

const config_python = "python";
const config_python_key_1 = "autoComplete.extraPaths";
const config_python_key_2 = "analysis.extraPaths";
const config_python_key_3 = "analysis.stubPath";
const config_python_value = `${ext?.extensionPath}\\code_completion`;

const config_micropython = "micropython";
const config_micropython_key = "codeCompletion.enabled";

// https://blog.csdn.net/forward_huan/article/details/108084802
function update_configuration(cfgName: string, key: string, value: any,
	configurationTarget: vscode.ConfigurationTarget | boolean, force: boolean = false) {
	return new Promise((resolve, reject) => {
		let cfg = vscode.workspace.getConfiguration(cfgName);

		if (force) {
			cfg.update(key, value, configurationTarget)
				.then(() => {
					resolve(true);
				})
				.then(undefined, error => {
					reject(error);
				});
		} else if (cfg.has(key)) {
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
	if (vscode.workspace.getConfiguration(config_micropython)
		.get(config_micropython_key) === true) {
		if (vscode.workspace.getConfiguration(config_python)
			.get(config_python_key_3) !== config_python_value) {
			vscode.commands.executeCommand('extension.enable', () => {});
		}
	}

	const enable = vscode.commands.registerCommand('extension.enable', () => {
		update_configuration(config_python, config_python_key_1, [config_python_value], vscode.ConfigurationTarget.Workspace)
		.then((resolved) => {
			if (resolved) {
				update_configuration(config_python, config_python_key_2, [config_python_value], vscode.ConfigurationTarget.Workspace)
				.then((resolved) => {
					if (resolved) {
						update_configuration(config_python, config_python_key_3, config_python_value, vscode.ConfigurationTarget.Workspace)
						.then(() => {
							update_configuration(config_micropython, config_micropython_key, true, vscode.ConfigurationTarget.Workspace, true);
							vscode.window.showInformationMessage(vscode.l10n.t("Update Settings Successed"));
						});
					}
				});
			} else {
				vscode.window.showErrorMessage(vscode.l10n.t("Update settings failed: Configuration key {0} not found.", config_python), vscode.l10n.t("OK"));
			}
		}).catch((error) => {
			vscode.window.showErrorMessage(vscode.l10n.t("Update settings failed: {0}", error.message), vscode.l10n.t("OK"));
		});
	});

	const disable = vscode.commands.registerCommand('extension.disable', () => {
		update_configuration(config_python, config_python_key_1, [], vscode.ConfigurationTarget.Workspace)
		.then((resolved) => {
			if (resolved) {
				update_configuration(config_python, config_python_key_2, [], vscode.ConfigurationTarget.Workspace)
				.then((resolved) => {
					if (resolved) {
						update_configuration(config_python, config_python_key_3, "", vscode.ConfigurationTarget.Workspace)
						.then(() => {
							update_configuration(config_micropython, config_micropython_key, false, vscode.ConfigurationTarget.Workspace);
							vscode.window.showInformationMessage(vscode.l10n.t("Update Settings Successed"));
						});
					}
				});
			} else {
				vscode.window.showErrorMessage(vscode.l10n.t("Update settings failed: Configuration key {0} not found.", config_python), vscode.l10n.t("OK"));
			}
		}).catch((error) => {
			vscode.window.showErrorMessage(vscode.l10n.t("Update settings failed: {0}", error.message), vscode.l10n.t("OK"));
		});
	});

	context.subscriptions.push(enable, disable);
}

export function deactivate() {}
