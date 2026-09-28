import json
import os

def update_notebook(filepath):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            src = ''.join(cell.get('source', []))
            if 'patients = pd.read_csv("patients.csv")' in src:
                # Replace the read_csv lines
                new_src = src.replace('patients = pd.read_csv("patients.csv")', 
'''import os

# Função para procurar os ficheiros automaticamente (evita erros de caminhos de pastas)
def find_file(filename, search_path="."):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    raise FileNotFoundError(f"Não foi possível encontrar o ficheiro '{filename}'.")

patients = pd.read_csv(find_file("patients.csv"))''')
                new_src = new_src.replace('rehab = pd.read_csv("rehabilitation.csv")', 'rehab = pd.read_csv(find_file("rehabilitation.csv"))')
                
                # Split back into lines
                lines = [line + '\n' for line in new_src.split('\n')]
                # remove the last newline if the original didn't have it
                if lines and not src.endswith('\n'):
                    lines[-1] = lines[-1].rstrip('\n')
                cell['source'] = lines

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

update_notebook('M0_G14.ipynb')
update_notebook('M0_G14_improved.ipynb')
