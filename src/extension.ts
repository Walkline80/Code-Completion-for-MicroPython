/* Copyright © 2024 Walkline Wang (https://walkline.wang)
 * Gitee: https://gitee.com/walkline/code-completion-for-micropython
 */
import * as vscode from 'vscode';

let ext = vscode.extensions.getExtension('walklinewang.code-completion-for-micropython');

const config_python = 'python';
const config_python_keys = [
	'autoComplete.extraPaths',
	'analysis.extraPaths',
	'analysis.stubPath'
];
let config_python_value = '';
const config_micropython = 'micropython';
const config_micropython_keys = [
	'enableCodeCompletion',
	'enableMultiLanguage'
];

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

async function get_code_completion_path() {
	const root = `${ext?.extensionPath}\\code_completion`;
	const path = vscode.Uri.file(`${root}\\${vscode.env.language}`);

	if (vscode.workspace.getConfiguration(config_micropython)
		.get(config_micropython_keys[1]) === true) {
		await vscode.workspace.fs.stat(path).then(
			(onfulfilled) => {
				config_python_value = path.fsPath;
			},
			(onrejected) => {
				config_python_value = `${root}\\default`;
			}
		);
	} else {
		config_python_value = `${root}\\default`;
	}
}

export async function activate(context: vscode.ExtensionContext) {
	await get_code_completion_path();

	if (vscode.workspace.getConfiguration(config_micropython)
		.get(config_micropython_keys[0]) === true) {
		if (vscode.workspace.getConfiguration(config_python)
			.get(config_python_keys[2]) !== config_python_value) {
			vscode.commands.executeCommand('extension.enable', () => {});
		}
	}

	const enable = vscode.commands.registerCommand('extension.enable', async () => {
		let success = false;
		try {
			success = await update_configuration(config_python, config_python_keys[0], [config_python_value], vscode.ConfigurationTarget.Workspace) as boolean;
			if (success) success = await update_configuration(config_python, config_python_keys[1], [config_python_value], vscode.ConfigurationTarget.Workspace) as boolean;
			if (success) success = await update_configuration(config_python, config_python_keys[2], config_python_value, vscode.ConfigurationTarget.Workspace) as boolean;
			if (success) {
				await update_configuration(config_micropython, config_micropython_keys[0], true, vscode.ConfigurationTarget.Workspace, true);
				vscode.window.showInformationMessage(vscode.l10n.t('Update Settings Successed'));
			} else {
				vscode.window.showErrorMessage(vscode.l10n.t('Update settings failed: Configuration key {0} not found.', config_python), vscode.l10n.t('OK'));
			}
		} catch (error: any) {
			vscode.window.showErrorMessage(vscode.l10n.t('Update settings failed: {0}', error.message), vscode.l10n.t('OK'));
		}
	});

	const disable = vscode.commands.registerCommand('extension.disable', async () => {
		let success = false;
		try {
			success = await update_configuration(config_python, config_python_keys[0], [], vscode.ConfigurationTarget.Workspace) as boolean;
			if (success) success = await update_configuration(config_python, config_python_keys[1], [], vscode.ConfigurationTarget.Workspace) as boolean;
			if (success) success = await update_configuration(config_python, config_python_keys[2], '', vscode.ConfigurationTarget.Workspace) as boolean;
			if (success) {
				await update_configuration(config_micropython, config_micropython_keys[0], false, vscode.ConfigurationTarget.Workspace);
				vscode.window.showInformationMessage(vscode.l10n.t('Update Settings Successed'));
			} else {
				vscode.window.showErrorMessage(vscode.l10n.t('Update settings failed: Configuration key {0} not found.', config_python), vscode.l10n.t('OK'));
			}
		} catch (error: any) {
			vscode.window.showErrorMessage(vscode.l10n.t('Update settings failed: {0}', error.message), vscode.l10n.t('OK'));
		}
	});

	vscode.commands.registerCommand('extension.codeCompletion', async () => {
		const enabled = await vscode.window.showQuickPick(
			[
				{label: vscode.l10n.t('Enable'),  description: vscode.l10n.t('Enable code completion'),  value: true},
				{label: vscode.l10n.t('Disable'), description: vscode.l10n.t('Disable code completion'), value: false}
			],
			{placeHolder: vscode.l10n.t('Whether to enable code completion or not?')});

		if (enabled) {
			if (enabled.value) {
				vscode.commands.executeCommand('extension.enable', () => {});
			} else {
				vscode.commands.executeCommand('extension.disable', () => {});
			}
		}
	});

	vscode.commands.registerCommand('extension.multiLanguage', async () => {
		const enabled = await vscode.window.showQuickPick(
			[
				{label: vscode.l10n.t('Enable'),  description: vscode.l10n.t('Enable multi-language documents support'),  value: true},
				{label: vscode.l10n.t('Disable'), description: vscode.l10n.t('Disable multi-language documents support'), value: false}
			],
			{placeHolder: vscode.l10n.t('Whether to enable multi-language documents or not?')});

		if (enabled) {
			update_configuration(config_micropython, config_micropython_keys[1], enabled.value, vscode.ConfigurationTarget.Workspace);

			const reload = await vscode.window.showQuickPick(
				[
					{label: '$(check)   YES', description: vscode.l10n.t('Reload window now'), value: true},
					{label: '$(close)   NO', description: vscode.l10n.t('Manually reload later'), value: false}
				],
				{placeHolder: vscode.l10n.t('Reload window now for the settings to take effect?')});

			if (reload?.value === true) {
				vscode.commands.executeCommand('workbench.action.reloadWindow');
			}
		}
	});
}

export function deactivate() {}
