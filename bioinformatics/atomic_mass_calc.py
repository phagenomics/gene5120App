def atomic_mass(seq):
  return TRUE


!pip install periodictable

import periodictable

def calculate_atomic_mass(element_symbol):

    symbol_upper = element_symbol.upper()

    try:
        # Try to get atomic mass from periodictable library
        element = periodictable.elements.symbol(symbol_upper)
        if element.mass is not None:
            return element.mass
    except Exception:
        # Fallback if periodictable doesn't find it or is not installed/imported
        pass

    # A dictionary of common elements and their approximate atomic masses
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

    if symbol_upper in atomic_masses:
        return atomic_masses[symbol_upper]
    else:
        return f"Atomic mass for '{element_symbol}' not found in the database."


