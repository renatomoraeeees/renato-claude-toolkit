import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
RELEASE = '2.1.1'


class ReleaseContractTests(unittest.TestCase):
    def test_release_versions_are_synchronized(self):
        plugin = json.loads((ROOT / 'plugins/master-developer/.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
        spec = importlib.util.spec_from_file_location(
            'release_catalog', ROOT / 'plugins/master-developer/scripts/catalog.py')
        catalog = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(catalog)

        self.assertEqual(RELEASE, plugin['version'])
        self.assertEqual(RELEASE, marketplace['version'])
        self.assertEqual(RELEASE, catalog.VERSION)

    def test_master_allows_auto_trigger_and_requires_skill_tool(self):
        master = (ROOT / 'plugins/master-developer/skills/master-developer/SKILL.md').read_text(encoding='utf-8')
        routing = (ROOT / 'plugins/master-developer/skills/master-developer/references/routing.md').read_text(encoding='utf-8')

        self.assertIn('disable-model-invocation: false', master)
        self.assertIn('tool `Skill`', master)
        self.assertIn('O catálogo não executa skills', master)
        self.assertIn('## Rota executável: descobrir, invocar, aplicar', routing)
        self.assertIn('não devem ser enviados à tool `Skill`', routing)


if __name__ == '__main__':
    unittest.main(verbosity=2)
