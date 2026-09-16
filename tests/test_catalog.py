import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import uuid
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'plugins/master-developer/scripts/catalog.py'
spec = importlib.util.spec_from_file_location('catalog', SCRIPT)
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        scratch = (Path(tempfile.gettempdir()) / 'claude-catalog-tests').resolve()
        scratch.mkdir(parents=True, exist_ok=True)
        self.root = scratch / str(uuid.uuid4())
        self.root.mkdir()
        assert self.root.resolve().is_relative_to(scratch)
        self.addCleanup(shutil.rmtree, self.root)
        self.config, self.project = self.root / 'config', self.root / 'projeto com acento é'
        self.plugin = self.root / 'cache/plugin'
        self.write(self.config / 'settings.json', {'enabledPlugins': {'demo@test': True}})
        self.write(self.config / 'plugins/installed_plugins.json', {'plugins': {'demo@test': [
            {'installPath': str(self.plugin), 'scope': 'user', 'version': '1'}]}})
        self.write(self.plugin / '.claude-plugin/plugin.json', {'name': 'demo'})

    def write(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value) if isinstance(value, dict) else value, encoding='utf-8')

    def skill(self, rel='skills/alpha/SKILL.md', name='alpha', extra='', description='Useful skill'):
        self.write(self.plugin / rel, f'---\nname: {name}\ndescription: {description}\n{extra}---\nBody')

    def collect(self):
        return catalog.collect(self.config, self.project)

    def test_custom_skills_add_default_but_commands_replace(self):
        self.write(self.plugin / '.claude-plugin/plugin.json',
                   {'name': 'demo', 'skills': ['./extra/'], 'commands': ['./selected/']})
        self.skill()
        self.skill('extra/beta/SKILL.md', 'beta')
        self.skill('commands/ignored.md', 'ignored')
        self.skill('selected/kept.md', 'kept')
        self.assertEqual({'demo:alpha', 'demo:beta', 'demo:kept'},
                         {c['qualified_name'] for c in self.collect()['components']})

    def test_marketplace_root_subset(self):
        market = self.root / 'market'
        self.write(self.config / 'plugins/known_marketplaces.json', {'test': {'installLocation': str(market)}})
        self.write(market / '.claude-plugin/marketplace.json',
                   {'plugins': [{'name': 'demo', 'source': './', 'skills': ['./selected/']}]})
        self.skill()
        self.skill('selected/beta/SKILL.md', 'beta')
        self.assertEqual(['demo:beta'], [c['qualified_name'] for c in self.collect()['components']])

    def test_root_skill_and_declared_name(self):
        self.skill('SKILL.md', 'stable-name')
        self.assertEqual('demo:stable-name', self.collect()['components'][0]['qualified_name'])

    def test_local_disable_overrides_global(self):
        self.skill()
        self.write(self.project / '.claude/settings.local.json', {'enabledPlugins': {'demo@test': False}})
        data = self.collect()
        self.assertFalse(data['components'][0]['automatic_candidate'])
        self.assertEqual([], catalog.search(data, 'alpha'))

    def test_other_project_install_is_not_candidate(self):
        self.skill()
        self.write(self.config / 'plugins/installed_plugins.json', {'plugins': {'demo@test': [
            {'installPath': str(self.plugin), 'scope': 'project', 'projectPath': str(self.root / 'other')}]}})
        self.assertEqual([], catalog.search(self.collect(), 'alpha'))

    def test_manual_yes_and_unknown_flags_are_excluded(self):
        self.skill(extra='disable-model-invocation: YES # manual\n')
        self.skill('skills/second/SKILL.md', 'second', extra='disable-model-invocation: perhaps\n')
        data = self.collect()
        self.assertTrue(data['components'][0]['manual_only'])
        self.assertEqual([], catalog.search(data, 'Useful skill', automatic=True))

    def test_duplicate_control_field_fails_closed(self):
        self.skill(extra='disable-model-invocation: true\ndisable-model-invocation: false\n')
        entry = self.collect()['components'][0]
        self.assertFalse(entry['automatic_candidate'])
        self.assertIn('duplicate_field:disable-model-invocation', entry['metadata_warnings'])

    def test_block_and_quoted_descriptions(self):
        self.skill(description='>\n  Review project\n  budget and schedule')
        self.assertEqual('Review project budget and schedule', self.collect()['components'][0]['description'])
        data, issues = catalog.metadata("---\nname: alpha\ndescription: 'Don''t lose # text'\n---\n")
        self.assertEqual("Don't lose # text", data['description'])
        self.assertFalse(issues)

    def test_wrappers_grouped_without_claiming_runtime_winner(self):
        self.skill()
        self.skill('commands/alpha.md')
        data = self.collect()
        self.assertEqual(1, len(data['collisions']))
        results = catalog.search(data, 'alpha')
        self.assertEqual(1, len(results))
        self.assertEqual(2, len(results[0]['variants']))
        self.assertIsNone(results[0]['session_visible'])

    def test_manual_collision_does_not_reenable_automatic_variant(self):
        self.skill()
        self.skill('commands/alpha.md', extra='disable-model-invocation: true\n')
        data = self.collect()
        self.assertEqual([], catalog.search(data, 'alpha', automatic=True))
        self.assertFalse(catalog.search(data, 'alpha')[0]['automatic_candidate'])

    def test_personal_project_and_skills_directory_plugin(self):
        self.write(self.config / 'skills/personal/SKILL.md', '---\nname: personal\ndescription: Personal\n---\n')
        self.write(self.project / '.claude/skills/project/SKILL.md', '---\nname: project\ndescription: Project\n---\n')
        embedded = self.project / '.claude/skills/bundle'
        self.write(embedded / '.claude-plugin/plugin.json', {'name': 'bundle'})
        self.write(embedded / 'SKILL.md', '---\nname: bundled\ndescription: Bundled\n---\n')
        self.assertEqual({'personal', 'project', 'bundle:bundled'},
                         {c['qualified_name'] for c in self.collect()['components']})

    def test_traversal_rejected(self):
        self.write(self.plugin / '.claude-plugin/plugin.json', {'name': 'demo', 'skills': ['../escape/']})
        self.write(self.plugin.parent / 'escape/SKILL.md', '---\nname: escape\ndescription: Outside\n---\n')
        data = self.collect()
        self.assertEqual([], data['components'])
        self.assertTrue(any(w['code'] == 'outside_component_root' for w in data['warnings']))

    def test_provider_configs_do_not_export_credentials_or_commands(self):
        self.write(self.plugin / '.mcp.json', {'mcpServers': {'browser': {'command': 'secret-command',
                   'env': {'TOKEN': 'sentinel-secret'}}}})
        self.write(self.plugin / 'hooks/hooks.json', {'hooks': {'Stop': [{'hooks': [
                   {'type': 'command', 'command': 'sentinel-secret'}]}]}})
        data = self.collect()
        serialized = json.dumps(data)
        self.assertNotIn('sentinel-secret', serialized)
        self.assertNotIn('secret-command', serialized)
        self.assertEqual(2, len(data['providers']))

    def test_changed_content_and_new_file_invalidate_fingerprint(self):
        self.skill()
        first = self.collect()['fingerprint']
        self.assertEqual(first, self.collect()['fingerprint'])
        self.skill(description='Different purpose')
        second = self.collect()['fingerprint']
        self.assertNotEqual(first, second)
        self.skill('skills/new/SKILL.md', 'new')
        self.assertNotEqual(second, self.collect()['fingerprint'])

    def test_portuguese_query_retrieves_english_description(self):
        self.skill(name='project-health', description='Analyze project health, budget and schedule')
        self.skill('skills/unrelated/SKILL.md', 'video', description='Video transcription')
        result = catalog.search(self.collect(), 'saúde e orçamento do projeto')
        self.assertEqual('demo:project-health', result[0]['qualified_name'])

    def test_atomic_output_is_valid_json_in_accented_path(self):
        target = self.project / '.claude/local/capabilities.json'
        catalog.atomic_write(target, self.collect())
        self.assertEqual(1, json.loads(target.read_text(encoding='utf-8'))['schema_version'])
        self.assertEqual([], list(target.parent.glob('*.tmp')))

    def test_multi_term_match_beats_generic_name_overlap(self):
        self.skill(name='planner', description='Analyze project health and budget')
        self.skill('skills/health/SKILL.md', 'health', description='Check network interfaces')
        self.assertEqual('demo:planner', catalog.search(self.collect(), 'project health budget')[0]['qualified_name'])

    def test_current_coordinator_can_be_excluded_without_hiding_others(self):
        self.skill(name='coordinator', description='Project budget coordinator')
        self.skill('skills/planner/SKILL.md', 'planner', description='Project budget planning')
        names = [r['qualified_name'] for r in catalog.search(self.collect(), 'project budget', exclude=['demo:coordinator'])]
        self.assertEqual(['demo:planner'], names)

    def test_bad_json_is_reported_without_crash(self):
        self.write(self.config / 'settings.json', '{broken')
        self.assertTrue(any(w['code'] == 'invalid_json' for w in self.collect()['warnings']))

    def test_read_views_are_bounded_complete_and_stable(self):
        for i in range(90):
            self.skill(f'skills/item-{i:03}/SKILL.md', f'item-{i:03}', description='漢字 revisão ' * 70)
        data = self.collect()
        destination = self.project / '.claude/local/capabilities.json'
        count = catalog.write_read_views(data, destination)
        self.assertGreater(count, 2)
        index = destination.parent / 'catalog-index.md'
        original_mtime = index.stat().st_mtime_ns
        links = catalog.re.findall(r'\]\(([^)]+)\)', index.read_text(encoding='utf-8'))
        pages = [(index.parent / p).read_text(encoding='utf-8') for p in links]
        self.assertTrue(all(len(page.encode('utf-8')) < 24000 for page in pages))
        for i in range(90):
            self.assertEqual(1, ''.join(pages).count(f'| demo:item-{i:03} |'))
        catalog.write_read_views(data, destination)
        self.assertEqual(original_mtime, index.stat().st_mtime_ns)

    def test_read_view_marks_manual_entries(self):
        self.skill(extra='disable-model-invocation: true\n')
        destination = self.project / '.claude/local/capabilities.json'
        catalog.write_read_views(self.collect(), destination)
        pages = list((destination.parent / 'catalog').rglob('*.md'))
        self.assertIn('| manual |', pages[0].read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
