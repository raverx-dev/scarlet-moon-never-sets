import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {QaInfrastructureError} from './errors.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
export const confineScript = path.join(here, 'chromium-confine.sh');

export function resolveBrowserLaunch(env = process.env) {
  const mode = env.QA_BROWSER_CONFINEMENT || 'required';
  if (mode !== 'required' && mode !== 'off') {
    throw new QaInfrastructureError('browser_confinement_invalid', 'QA_BROWSER_CONFINEMENT must be required or off');
  }
  if (mode === 'off') {
    if (env.CREDENTIALS_DIRECTORY) {
      throw new QaInfrastructureError('browser_confinement_required', 'browser confinement cannot be disabled while CREDENTIALS_DIRECTORY is set');
    }
    return {confined: false};
  }
  if (!fs.existsSync('/usr/bin/bwrap')) {
    throw new QaInfrastructureError('browser_confinement_unavailable', 'bubblewrap is required for browser confinement');
  }
  if (!fs.existsSync(confineScript)) {
    throw new QaInfrastructureError('browser_confinement_unavailable', 'Chromium confinement launcher is missing');
  }
  return {confined: true, executable: confineScript};
}
