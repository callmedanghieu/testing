#!/usr/bin/env bash
# Run every check that is possible on this machine.
set -e
cd "$(dirname "$0")"
python3 tools/build.py
python3 -m unittest tests.test_system -v
if command -v mysql >/dev/null || command -v psql >/dev/null; then
  tools/start_servers.sh || true
  python3 -m unittest tests.test_servers -v
fi
if command -v node >/dev/null; then
  node tests/test_engine.js
  if NODE_PATH=$(npm root -g) node -e 'require("playwright")' 2>/dev/null; then
    NODE_PATH=$(npm root -g) node tests/test_app_browser.js
  fi
fi
