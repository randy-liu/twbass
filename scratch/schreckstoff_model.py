import numpy as np

def calculate_dead_zone():
    # Parameters
    # Alarm response threshold (ART) for largemouth bass (estimated free concentration threshold)
    # Let's say baseline 8m is achieved with:
    # M = 1000 mg (released from skin damage of hooked fish)
    # D_pure = 5.0e-6 cm^2/s = 5.0e-10 m^2/s
    # C_threshold = 1.0e-7 mg/L = 1.0e-10 g/m^3 (approximate threshold)
    # In pure water, no decay:
    # C(r, t) = M / (4 * pi * D * t)^(1.5) * exp(-r^2 / (4 * D * t))
    # The maximum concentration at r is reached at t = r^2 / (6 * D)
    # C_max(r) = M / (4 * pi * D * (r^2 / (6 * D)))^(1.5) * exp(-1.5)
    #          = M / (2/3 * pi * r^2)^(1.5) * exp(-1.5)
    # Let's calibrate M and C_threshold to match baseline r_max = 8.0 m in pure water.
    # C_max(8.0) = M / ( (2/3) * pi * 8.0^2 )^1.5 * exp(-1.5) = C_threshold
    # Let's use this to establish a baseline model.
    
    # We will test three zones:
    # Zone-A: DOC = 12 mg/L, pH = 5.5, K_doc = 6.0e4 L/kg_oc
    # Zone-B: DOC = 8 mg/L, pH = 6.2, K_doc = 4.5e4 L/kg_oc
    # Zone-C: DOC = 3 mg/L, pH = 7.2, K_doc = 2.0e4 L/kg_oc
    
    zones = {
        'Pure Water (Baseline)': {'DOC': 0.0, 'pH': 7.0, 'K_doc': 0.0, 'k_bio': 0.0, 'k_photo': 0.0},
        'Zone-A (Northern Windward)': {'DOC': 12.0, 'pH': 5.5, 'K_doc': 6.0e4, 'k_bio': 0.15, 'k_photo': 0.35}, # rates in hr^-1
        'Zone-B (Northern Leeward)': {'DOC': 8.0, 'pH': 6.2, 'K_doc': 4.5e4, 'k_bio': 0.12, 'k_photo': 0.28},
        'Zone-C (Southern)': {'DOC': 3.0, 'pH': 7.2, 'K_doc': 2.0e4, 'k_bio': 0.08, 'k_photo': 0.15}
    }
    
    M = 50.0 # mg released (total pool)
    D_free = 5.0e-6 * 1e-4 * 3600 # m^2/hr = 1.8e-5 m^2/hr
    C_threshold = 1.0e-6 # mg/m^3 (equivalent to 1 pg/mL)
    
    print(f"D_free: {D_free:.2e} m^2/hr")
    
    for name, params in zones.items():
        doc_kg_L = params['DOC'] * 1e-6 # mg/L to kg/L
        K_doc = params['K_doc'] # L/kg
        R = 1.0 + K_doc * doc_kg_L
        f_free = 1.0 / R
        
        # Effective diffusion: humic acid is a macromolecule with D_ha ~ 1e-7 cm^2/s, virtually immobile compared to free H3NO.
        # D_eff = f_free * D_free + f_bound * D_ha ~ f_free * D_free
        D_eff = f_free * D_free
        
        # Decay rate (hr^-1)
        k_total = params['k_bio'] + params['k_photo']
        
        # Let's find r_max where C_free(r, t) >= C_threshold
        # We search r from 0 to 15 m
        r_arr = np.linspace(0.01, 15.0, 1500)
        c_max_r = []
        t_max_r = []
        
        for r in r_arr:
            # We find t that maximizes C_free(r, t)
            # C_free(r, t) = f_free * M / (4 * pi * D_eff * t)^1.5 * exp(-r^2 / (4 * D_eff * t) - k_total * t)
            # Let's search t from 0.01 to 100 hr
            t_search = np.linspace(0.001, 150.0, 15000)
            c_vals = (f_free * M / (4 * np.pi * D_eff * t_search)**1.5) * np.exp(-r**2 / (4 * D_eff * t_search) - k_total * t_search)
            idx_max = np.argmax(c_vals)
            c_max_r.append(c_vals[idx_max])
            t_max_r.append(t_search[idx_max])
            
        c_max_r = np.array(c_max_r)
        
        # Find the maximum radius where c_max_r >= C_threshold
        valid_indices = np.where(c_max_r >= C_threshold)[0]
        if len(valid_indices) > 0:
            r_max = r_arr[valid_indices[-1]]
            t_at_r_max = t_max_r[valid_indices[-1]]
        else:
            r_max = 0.0
            t_at_r_max = 0.0
            
        area = np.pi * r_max**2
        print(f"\n--- {name} ---")
        print(f"DOC: {params['DOC']} mg/L, pH: {params['pH']}")
        print(f"Retardation factor R: {R:.3f}, Free fraction f_free: {f_free:.3%}")
        print(f"Effective Diffusion D_eff: {D_eff:.2e} m^2/hr")
        print(f"Decay rate k_total: {k_total:.2e} hr^-1 (Half-life: {np.log(2)/k_total:.2f} hr)" if k_total > 0 else "Decay rate: 0")
        print(f"Max Dead Zone Radius r_max: {r_max:.2f} m")
        print(f"Dead Zone Area: {area:.2f} m^2")
        print(f"Time to reach max radius: {t_at_r_max:.2f} hr")

if __name__ == '__main__':
    calculate_dead_zone()
