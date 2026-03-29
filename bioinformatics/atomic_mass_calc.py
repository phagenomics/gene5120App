def atomic_mass(seq):
  return TRUE



    # A dictionary of common elements and atomic masses
    atomic_masses = {
        'H': 1.008,
        'He': 4.0026,
        'Li': 6.94,
        'Be': 9.0122,
        'B': 10.81,
        'C': 12.011,
        'N': 14.007,
        'O': 15.999,
        'F': 18.998,
        'Ne': 20.180,
        'Na': 22.990,
        'Mg': 24.305,
        'Al': 26.982,
        'Si': 28.085,
        'P': 30.974,
        'S': 32.06,
        'Cl': 35.45,
        'Ar': 39.948,
        'K': 39.098,
        'Ca': 40.078,
        'Au': 196.96657 # Added Gold for demonstration
    }
# function
def get_atomic_mass(element):
    return atomic_masses.get(element, "Element not found")

# test
print(get_atomic_mass("C"))   # 12.011
print(get_atomic_mass("O"))   # 15.999

def molecular_mass(formula_dict):
    total_mass = 0
    
    for element, count in formula_dict.items():
        mass = atomic_masses.get(element)
        
        if mass is None:
            print(f"Unknown element: {element}")
            return None
        
        total_mass += mass * count
    
    return total_mass

