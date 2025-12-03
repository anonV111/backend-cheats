import re
import subprocess
import sys
from pathlib import Path

def fix_markdown(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace '-   ### Heading' with '### Heading' on its own line
    content = re.sub(r'^\s*-\s{3}(#{3,6} .*)$', r'\1', content, flags=re.MULTILINE)

    # Remove exactly 4 leading spaces from any line starting with 4 spaces (paragraphs, images, nested blocks)
    content = re.sub(r'^\ {4}', '', content, flags=re.MULTILINE)

    content = re.sub(r'<div align="right"><a href="#top">Contents ⬆️</a></div>', '', content)
    
    Path(output_path).write_text(content, encoding='utf-8')
    print(f"✅ Fixed Markdown saved to {output_path}")

def post_process_gitbook():
    """Post-process after mdsplit: rename, delete, edit toc.md"""
    contents_dir = Path("gitbook/contents")
    
    # 1. Rename README_fixed.md → README.md
    readme_fixed = contents_dir / "README_fixed.md"
    readme_new = contents_dir / "README.md"
    if readme_fixed.exists():
        readme_fixed.rename(readme_new)
        print("✅ Renamed README_fixed.md → README.md")
    
    # 2. Remove Contents.md
    contents_md = contents_dir / "Contents.md"
    if contents_md.exists():
        contents_md.unlink()
        print("🗑️  Removed Contents.md")
    
    # 3. Fix toc.md
    toc_md = contents_dir / "toc.md"
    if toc_md.exists():
        with open(toc_md, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix README_fixed → README
        content = re.sub(r'- \[README_fixed\]\(<\./README_fixed\.md>\)', r'- [README](<./README.md>)', content)
        # Remove Contents line
        content = re.sub(r'- \[Contents\]\(<\./Contents\.md>\)\n?', '', content, flags=re.MULTILINE)
        # Clean extra blank lines
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        with open(toc_md, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Fixed toc.md")

def fix_image_paths():
    """Fix ./files/ paths to ../../../original/files/ based on folder depth"""
    contents_dir = Path("gitbook/contents")
    
    for md_file in contents_dir.rglob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Calculate depth: contents/ (1) → Network--Internet/ (2) → file.md (3) = 2 '../'
        rel_path = md_file.relative_to(contents_dir)
        depth = len(rel_path.parent.parts) if rel_path.parent != Path('.') else 0
        up_levels = '../' * (depth + 2)
        
        # Fix Markdown images: ![alt](./files/...) → ![alt](../../../original/files/...)
        content = re.sub(
            r'(\!\[.*?\]\()(\./files/)([^)]+)(\))',
            rf'\1{up_levels}original/files/\3\4',
            content
        )
        
        # Fix HTML images: <img src="./files/..."> → <img src="../../../original/files/...">
        content = re.sub(
            r'(src=")(\./files/)([^"]+)(")',
            rf'\1{up_levels}original/files/\3\4',
            content
        )
        
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        

if __name__ == "__main__":
    fix_markdown("original/README.md", "original/README_fixed.md")
    
    contents_dir = Path("gitbook/contents")
    if contents_dir.exists():
        import shutil
        shutil.rmtree(contents_dir)
    contents_dir.mkdir(parents=True, exist_ok=True)
    
    cmd = ["mdsplit", "original/README_fixed.md", "--output", "gitbook/contents", "--max-level", "3", "--force","-t"]
    result = subprocess.run(cmd, capture_output=True, text=True)
        
    if result.returncode == 0:
        print("✅ mdsplit completed successfully!")
        post_process_gitbook()  
        fix_image_paths()
        print("📁 GitBook is ready in 'gitbook/contents/'")
    else:
        print("❌ mdsplit failed:")
        print(result.stderr)
        sys.exit(1)