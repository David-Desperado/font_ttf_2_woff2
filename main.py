import os
from fontTools.ttLib import TTFont

def convert_fonts():
    # Define import and export directories
    base_dir = os.path.dirname(os.path.abspath(__file__))
    import_dir = os.path.join(base_dir, "import")
    export_dir = os.path.join(base_dir, "export")
    
    # Ensure export directory exists
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    # Loop through all files in the import directory
    for filename in os.listdir(import_dir):
        # Added .otf to the check below!
        if filename.lower().endswith((".ttf", ".otf")):
            input_path = os.path.join(import_dir, filename)
            name = os.path.splitext(filename)[0]
            print(f"Converting: {filename}")
            
            try:
                # Open the Font
                with TTFont(input_path) as font:
                    
                    # Save as WOFF (commented out)
                    # font.flavor = 'woff'
                    # font.save(os.path.join(export_dir, f"{name}.woff"))
                    
                    # Save as WOFF2
                    font.flavor = 'woff2'
                    font.save(os.path.join(export_dir, f"{name}.woff2"))
                    
                print(f"Success! Created {name}.woff2 in export/ ✅")
                
            except Exception as e:
                print(f"Error converting {filename}: {e} ❌")

if __name__ == "__main__":
    convert_fonts()
