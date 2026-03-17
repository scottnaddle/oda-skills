#!/usr/bin/env python3
"""
ODA Skills Marketplace Validator
Validates marketplace.json and all plugin structures against Claude Code spec.
Usage: python3 validate_plugins.py
"""

import json
import os
import sys
import re
from pathlib import Path

ERRORS = []
WARNINGS = []

def error(msg):
    ERRORS.append(msg)
    print(f"  ❌ {msg}")

def warn(msg):
    WARNINGS.append(msg)
    print(f"  ⚠️  {msg}")

def ok(msg):
    print(f"  ✅ {msg}")

def validate_marketplace():
    print("\n=== Validating marketplace.json ===")
    mp_path = Path(".claude-plugin/marketplace.json")
    if not mp_path.exists():
        error("Missing .claude-plugin/marketplace.json")
        return None
    
    try:
        mp = json.loads(mp_path.read_text())
    except json.JSONDecodeError as e:
        error(f"Invalid JSON in marketplace.json: {e}")
        return None
    
    # Required fields
    if "name" not in mp:
        error("marketplace.json: missing 'name'")
    else:
        ok(f"name: {mp['name']}")
    
    if "owner" not in mp:
        error("marketplace.json: missing 'owner'")
    elif "name" not in mp.get("owner", {}):
        error("marketplace.json: owner missing 'name'")
    else:
        ok(f"owner: {mp['owner']['name']}")
    
    if "plugins" not in mp:
        error("marketplace.json: missing 'plugins' array")
        return None
    
    ok(f"plugins: {len(mp['plugins'])} entries")
    
    for p in mp["plugins"]:
        if "name" not in p:
            error(f"Plugin entry missing 'name'")
        if "source" not in p:
            error(f"Plugin '{p.get('name', '?')}': missing 'source'")
        else:
            source_path = Path(p["source"])
            if not source_path.exists():
                error(f"Plugin '{p['name']}': source path '{p['source']}' not found")
    
    return mp

def validate_plugin(plugin_dir):
    name = plugin_dir.name
    print(f"\n=== Validating plugin: {name} ===")
    
    # Check plugin.json
    pj_path = plugin_dir / ".claude-plugin" / "plugin.json"
    if not pj_path.exists():
        error(f"{name}: missing .claude-plugin/plugin.json")
        return
    
    try:
        pj = json.loads(pj_path.read_text())
    except json.JSONDecodeError as e:
        error(f"{name}: invalid JSON in plugin.json: {e}")
        return
    
    # Required fields
    for field in ["name", "version", "description"]:
        if field not in pj:
            error(f"{name}/plugin.json: missing '{field}'")
        else:
            if field == "name" and pj["name"] != name:
                warn(f"{name}/plugin.json: name '{pj['name']}' doesn't match directory '{name}'")
    
    ok(f"plugin.json valid — {pj.get('name', '?')} v{pj.get('version', '?')}")
    
    # Check skills
    skills_dir = plugin_dir / "skills"
    if skills_dir.exists():
        skill_count = 0
        for skill_dir in sorted(skills_dir.iterdir()):
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                error(f"{name}/skills/{skill_dir.name}: missing SKILL.md")
                continue
            
            # Validate SKILL.md frontmatter
            content = skill_md.read_text()
            if not content.startswith("---"):
                error(f"{name}/skills/{skill_dir.name}/SKILL.md: missing YAML frontmatter")
                continue
            
            parts = content.split("---", 2)
            if len(parts) < 3:
                error(f"{name}/skills/{skill_dir.name}/SKILL.md: malformed frontmatter")
                continue
            
            fm = parts[1].strip()
            has_name = any(line.strip().startswith("name:") for line in fm.split("\n"))
            has_desc = any(line.strip().startswith("description:") for line in fm.split("\n"))
            
            if not has_name:
                error(f"{name}/skills/{skill_dir.name}/SKILL.md: frontmatter missing 'name'")
            if not has_desc:
                error(f"{name}/skills/{skill_dir.name}/SKILL.md: frontmatter missing 'description'")
            
            # Check name matches directory
            for line in fm.split("\n"):
                if line.strip().startswith("name:"):
                    fm_name = line.split(":", 1)[1].strip()
                    if fm_name != skill_dir.name:
                        warn(f"{name}/skills/{skill_dir.name}: frontmatter name '{fm_name}' != dir name '{skill_dir.name}'")
            
            # Check line count
            lines = len(content.split("\n"))
            if lines > 500:
                warn(f"{name}/skills/{skill_dir.name}/SKILL.md: {lines} lines (recommended < 500)")
            
            skill_count += 1
        
        ok(f"{skill_count} skills validated")
    else:
        warn(f"{name}: no skills/ directory")
    
    # Check commands
    cmds_dir = plugin_dir / "commands"
    if cmds_dir.exists():
        cmd_count = 0
        for cmd_file in sorted(cmds_dir.glob("*.md")):
            content = cmd_file.read_text()
            if not content.startswith("---"):
                error(f"{name}/commands/{cmd_file.name}: missing YAML frontmatter")
                continue
            
            parts = content.split("---", 2)
            if len(parts) < 3:
                error(f"{name}/commands/{cmd_file.name}: malformed frontmatter")
                continue
            
            fm = parts[1].strip()
            has_desc = any(line.strip().startswith("description:") for line in fm.split("\n"))
            if not has_desc:
                error(f"{name}/commands/{cmd_file.name}: frontmatter missing 'description'")
            
            cmd_count += 1
        
        ok(f"{cmd_count} commands validated")
    else:
        warn(f"{name}: no commands/ directory")
    
    # Check README
    readme = plugin_dir / "README.md"
    if not readme.exists():
        warn(f"{name}: no README.md")
    else:
        ok("README.md present")

def main():
    print("=" * 50)
    print("ODA Skills Marketplace Validator")
    print("=" * 50)
    
    mp = validate_marketplace()
    
    # Validate each plugin directory
    for plugin_dir in sorted(Path(".").glob("oda-*")):
        if plugin_dir.is_dir():
            validate_plugin(plugin_dir)
    
    # Summary
    print("\n" + "=" * 50)
    print("VALIDATION SUMMARY")
    print("=" * 50)
    
    if ERRORS:
        print(f"\n❌ {len(ERRORS)} error(s)")
        for e in ERRORS:
            print(f"   - {e}")
    
    if WARNINGS:
        print(f"\n⚠️  {len(WARNINGS)} warning(s)")
        for w in WARNINGS:
            print(f"   - {w}")
    
    if not ERRORS and not WARNINGS:
        print("\n✅ All validations passed!")
    elif not ERRORS:
        print(f"\n✅ No errors. {len(WARNINGS)} warning(s) to review.")
    else:
        print(f"\n❌ {len(ERRORS)} error(s) must be fixed before publishing.")
    
    return 1 if ERRORS else 0

if __name__ == "__main__":
    sys.exit(main())
