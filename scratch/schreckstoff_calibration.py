import numpy as np

def calibrate_and_simulate():
    # Model parameters
    M = 1000.0 # mg (amount of Schreckstoff released from injured skin)
    D_turbulent = 0.5 # m^2/hr (turbulent eddy diffusion coefficient in static pond)
    
    # We want C_max(8.0) in pure water to be equal to C_threshold
    # Let's calculate C_threshold such that r_max = 8.0 m in pure water with k = 0
    # For a point source: C(r, t) = M / (4 * pi * D * t)^1.5 * exp(-r^2 / (4 * D * t))
    # C_max(r) is achieved when t = r^2 / (6 * D)
    # C_max(r) = M / (4 * pi * D * (r^2 / (6 * D)))^1.5 * exp(-1.5)
    #          = M / (2/3 * pi * r^2)^1.5 * exp(-1.5)
    r_base = 8.0
    C_threshold = M / ( (2/3.0) * np.pi * r_base**2 )**1.5 * np.exp(-1.5)
    
    print(f"Calibrated C_threshold: {C_threshold:.4e} mg/m^3")
    
    # Now let's define the parameters for each Zone
    # DOC (mg/L), pH, K_doc (L/kg_oc), k_bio (hr^-1), k_photo (hr^-1)
    zones = {
        'Pure Water (Baseline)': {'DOC': 0.0, 'pH': 7.0, 'K_doc': 0.0, 'k_bio': 0.0, 'k_photo': 0.0},
        'Zone-A (Northern Windward)': {'DOC': 12.0, 'pH': 5.5, 'K_doc': 6.0e4, 'k_bio': 0.15, 'k_photo': 0.35},
        'Zone-B (Northern Leeward)': {'DOC': 8.0, 'pH': 6.2, 'K_doc': 4.5e4, 'k_bio': 0.12, 'k_photo': 0.28},
        'Zone-C (Southern)': {'DOC': 3.0, 'pH': 7.2, 'K_doc': 2.0e4, 'k_bio': 0.08, 'k_photo': 0.15}
    }
    
    for name, params in zones.items():
        doc_kg_L = params['DOC'] * 1e-6 # mg/L to kg/L
        K_doc = params['K_doc'] # L/kg
        R = 1.0 + K_doc * doc_kg_L
        f_free = 1.0 / R
        
        # Effective diffusion: humic acid is large and has low diffusion, so the bound fraction is effectively immobile.
        # D_eff = f_free * D_turbulent
        D_eff = f_free * D_turbulent
        
        k_total = params['k_bio'] + params['k_photo']
        
        r_arr = np.linspace(0.01, 15.0, 1500)
        c_max_r = []
        t_max_r = []
        
        for r in r_arr:
            # Search for t that maximizes C_free(r, t)
            t_search = np.linspace(0.001, 100.0, 10000)
            c_vals = (f_free * M / (4 * np.pi * D_eff * t_search)**1.5) * np.exp(-r**2 / (4 * D_eff * t_search) - k_total * t_search)
            idx_max = np.argmax(c_vals)
            c_max_r.append(c_vals[idx_max])
            t_max_r.append(t_search[idx_max])
            
        c_max_r = np.array(c_max_r)
        
        valid_indices = np.where(c_max_r >= C_threshold)[0]
        if len(valid_indices) > 0:
            r_max = r_arr[valid_indices[-1]]
            t_at_r_max = t_max_r[valid_indices[-1]]
        else:
            r_max = 0.0
            t_at_r_max = 0.0
            
        # Let's calculate concentration reduction rate at 1m, 2m, 5m from source
        # relative to the pure water baseline at the same distance
        reductions = {}
        for dist in [1.0, 2.0, 5.0]:
            # Baseline max concentration in pure water at dist
            # C_base_max(dist) = M / (2/3 * pi * dist^2)^1.5 * exp(-1.5)
            c_base_max = M / ( (2/3.0) * np.pi * dist**2 )**1.5 * np.exp(-1.5)
            
            # Max concentration in this Zone at dist
            t_search = np.linspace(0.001, 100.0, 10000)
            c_vals_zone = (f_free * M / (4 * np.pi * D_eff * t_search)**1.5) * np.exp(-dist**2 / (4 * D_eff * t_search) - k_total * t_search)
            c_zone_max = np.max(c_vals_zone)
            
            pct_reduction = (1.0 - c_zone_max / c_base_max) * 100
            reductions[dist] = (c_zone_max, pct_reduction)
            
        area = np.pi * r_max**2
        print(f"\n--- {name} ---")
        print(f"DOC: {params['DOC']} mg/L, pH: {params['pH']}")
        print(f"Retardation factor R: {R:.3f}, Free fraction f_free: {f_free:.3%}")
        print(f"Effective Diffusion D_eff: {D_eff:.4f} m^2/hr")
        print(f"Decay rate k_total: {k_total:.2f} hr^-1 (Half-life: {np.log(2)/k_total:.2f} hr)" if k_total > 0 else "Decay rate: 0")
        print(f"Max Dead Zone Radius r_max: {r_max:.2f} m")
        print(f"Dead Zone Area: {area:.2f} m^2")
        print(f"Time to reach max radius: {t_at_r_max:.2f} hr")
        for dist, (val, red) in reductions.items():
            print(f"  At {dist}m: Max Free Conc = {val:.4e} mg/m^3 (Reduction: {red:.2f}%)")

if __name__ == '__main__':
    calibrate_and_simulate()
