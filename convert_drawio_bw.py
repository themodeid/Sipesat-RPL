import os
import re
import xml.etree.ElementTree as ET

RPL_DIR = r"c:\A_main_code\all-my-projek\RPL"

def convert_style_to_bw(style_str, cell_id=""):
    if not style_str:
        return style_str
    
    parts = style_str.split(";")
    new_parts = []
    
    cid_lower = cell_id.lower()
    
    # 1. Detect start / initial nodes (solid black circle)
    is_initial_node = False
    if "ellipse" in style_str and "doubleellipse" not in style_str.lower():
        if cid_lower in ["act_r1_sym", "sm_init", "auth_init", "s_start", "d1", "f1", "a1"]:
            is_initial_node = True
        elif cid_lower.endswith("_init") or cid_lower.endswith("_start"):
            is_initial_node = True

    # 2. Detect end / final nodes (double ellipse bullseye)
    is_double_ellipse = "doubleellipse" in style_str.lower()
    if cid_lower in ["act_r5_sym", "sm_final", "auth_final", "s_end", "d13", "f14", "a14"]:
        is_double_ellipse = True
    elif cid_lower.endswith("_final") or cid_lower.endswith("_end"):
        is_double_ellipse = True

    # 3. Detect table headers (subtle light gray shading for contrast)
    is_table_header = False
    if cid_lower.startswith("th_") or cid_lower.startswith("act_th") or cid_lower.startswith("seq_th") or cid_lower in ["row_header", "act_row_th", "seq_row_th"]:
        is_table_header = True

    # 4. Detect alternating table rows
    is_alt_row = False
    if re.search(r'row_[02468]', cid_lower) or re.search(r'c[02468]_', cid_lower):
        is_alt_row = True

    for p in parts:
        if not p.strip():
            continue
        key_val = p.split("=", 1)
        k = key_val[0].strip()
        v = key_val[1].strip() if len(key_val) > 1 else ""
        
        if k == "strokeColor":
            if v == "none":
                new_parts.append("strokeColor=none")
            else:
                new_parts.append("strokeColor=#000000")
        elif k == "fontColor":
            new_parts.append("fontColor=#000000")
        elif k == "fillColor":
            if v == "none":
                new_parts.append("fillColor=none")
            elif is_initial_node:
                new_parts.append("fillColor=#000000")
            elif is_double_ellipse:
                new_parts.append("fillColor=#000000")
            elif is_table_header:
                new_parts.append("fillColor=#f1f5f9")
            elif is_alt_row:
                new_parts.append("fillColor=#f8fafc")
            else:
                new_parts.append("fillColor=#ffffff")
        elif k == "labelBackgroundColor":
            new_parts.append("labelBackgroundColor=#ffffff")
        else:
            new_parts.append(p)
            
    # Always ensure fontColor=#000000
    if not any(p.startswith("fontColor=") for p in new_parts):
        new_parts.append("fontColor=#000000")
        
    return ";".join(new_parts)

def clean_inline_html_bw(val_str):
    if not val_str:
        return val_str
    
    cleaned = val_str
    # Replace any color hex with #000000
    cleaned = re.sub(r'color:\s*#[0-9a-fA-F]{3,6}', 'color:#000000', cleaned)
    # Replace background hex with #ffffff or remove
    cleaned = re.sub(r'background(?:-color)?:\s*#[0-9a-fA-F]{3,6}', 'background-color:#ffffff', cleaned)
    # Remove emoji icons so it looks strictly clean & academic
    cleaned = cleaned.replace("🏛️ ", "").replace("📋 ", "").replace("🔄 ", "").replace("🔐 ", "")
    return cleaned

def convert_file(filename):
    filepath = os.path.join(RPL_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    tree = ET.fromstring(content)
    
    for cell in tree.iter("mxCell"):
        cell_id = cell.get("id", "")
        style = cell.get("style", "")
        value = cell.get("value", "")
        
        if style:
            cell.set("style", convert_style_to_bw(style, cell_id))
        if value:
            cell.set("value", clean_inline_html_bw(value))
            
    bw_content = ET.tostring(tree, encoding="utf-8").decode("utf-8")
    if not bw_content.startswith("<mxfile"):
        bw_content = f'<mxfile host="65bd71144e">\n{bw_content}\n</mxfile>'
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(bw_content)
    print(f"[OK] Converted to Black & White: {filepath}")

def main():
    # 1. First recreate base files from master
    print("Rebuilding clean base from master...")
    os.system(f"python {os.path.join(RPL_DIR, 'build_rpl_drawio.py')}")
    
    # 2. Convert all 3 files to pure Black & White
    print("Applying Black & White styling...")
    for fn in ["tugas-3-usecase.drawio", "tugas-4-activity-sequence.drawio", "tugas-5-state-machine.drawio"]:
        convert_file(fn)

if __name__ == "__main__":
    main()
