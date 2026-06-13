#!/usr/bin/env node
// Propagate the canonical version from the root package.json (bumped by
// `changeset version`) into the plugin manifests that actually ship.
//
// The plugin is distributed through two manifests that each carry their own
// `version` field. Rather than bump them by hand (and risk drift), changesets
// owns the version in package.json and this script mirrors it outward.
//
// Run automatically by the `version-packages` npm script, right after
// `changeset version`. Safe to run on its own at any time — it only touches
// the `version` field and preserves each file's key order and formatting.

import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');

const { version } = JSON.parse(readFileSync(join(root, 'package.json'), 'utf8'));

const targets = ['.claude-plugin/plugin.json', '.codex-plugin/plugin.json'];

let changed = 0;
for (const rel of targets) {
  const path = join(root, rel);
  const manifest = JSON.parse(readFileSync(path, 'utf8'));
  if (manifest.version === version) {
    console.log(`= ${rel} already at ${version}`);
    continue;
  }
  const from = manifest.version;
  manifest.version = version;
  writeFileSync(path, JSON.stringify(manifest, null, 2) + '\n');
  console.log(`✓ ${rel} ${from} → ${version}`);
  changed++;
}

console.log(`Synced ${version} into ${changed} manifest(s).`);
