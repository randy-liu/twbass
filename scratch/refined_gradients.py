import numpy as np

def simulate_refined():
    # 1. Fe2+ vertical gradient (Northern Ultisol water - Oxic-decay model)
    # C(z) = C_0 * exp(-z / lambda)
    # J_0 = D_z * C_0 / lambda => C_0 = J_0 * lambda / D_z
    # lambda = sqrt(D_z / k_x)
    # D_z (bottom eddy diffusion under weak wind) = 1.0e-4 cm^2/s = 0.864 m^2/day
    D_z_fe = 1.0e-4 * 1e-4 * 86400 # 0.864 m^2/day
    
    # pH 6.2 (Zone-B) vs pH 5.5 (Zone-A, high DOC inhibits oxidation)
    k_fe_B = 0.28 # day^-1 (half-life 2.5 days)
    k_fe_A = 0.12 # day^-1 (half-life 5.8 days)
    
    fe_flux_low = 10.0 * 55.85 # mg/m^2/day
    fe_flux_high = 50.0 * 55.85 # mg/m^2/day
    
    thr_fe_damage = 0.35 # mg/L
    thr_fe_avoid = 0.10 # mg/L
    
    print("=== REFINED Fe2+ GRADIENTS (Northern Ultisol) ===")
    for name, J_0, k_x in [('Zone-B (Spring, Low Flux, 10 mmol/m^2/day)', fe_flux_low, k_fe_B),
                           ('Zone-A (Summer, High Flux, 50 mmol/m^2/day)', fe_flux_high, k_fe_A)]:
        lam = np.sqrt(D_z_fe / k_x)
        C_0 = (J_0 * lam) / D_z_fe / 1000.0 # mg/L
        
        print(f"\n--- {name} ---")
        print(f"  lambda: {lam*100:.2f} cm, C_0: {C_0:.3f} mg/L")
        for z_cm in [10, 30, 50, 100]:
            c_z = C_0 * np.exp(-z_cm / (lam * 100.0))
            print(f"  At {z_cm} cm: {c_z:.3f} mg/L")
        z_dmg = -lam * 100.0 * np.log(thr_fe_damage / C_0) if C_0 > thr_fe_damage else 0
        z_avd = -lam * 100.0 * np.log(thr_fe_avoid / C_0) if C_0 > thr_fe_avoid else 0
        print(f"  Safety Distance (Gill Damage, 0.35 mg/L): {z_dmg:.1f} cm")
        print(f"  Safety Distance (Avoidance, 0.10 mg/L): {z_avd:.1f} cm")
        
    # 2. H2S vertical gradient (Southern Inceptisol water)
    # We test two models:
    # Model 1: Oxic-decay model (aerated pond or shallow water with some DO near bottom)
    # Model 2: Stratified Anoxic-Interface model (stagnant summer or night shutdown, where bottom h = 1.0 m or 1.5 m is anoxic, k_x = 0)
    # In Model 2: C(z) = (J_0 / D_z) * (h - z) for z <= h, and 0 for z > h.
    # D_z_stagnant = 2.0e-5 cm^2/s = 0.1728 m^2/day
    # D_z_mixed = 2.0e-4 cm^2/s = 1.728 m^2/day
    
    h2s_flux_low = 19.0 * 34.08 # mg/m^2/day
    h2s_flux_high = 281.0 * 34.08 # mg/m^2/day
    
    thr_h2s_avoid = 0.002 # mg/L
    thr_h2s_acute = 0.05 # mg/L
    
    print("\n=== REFINED H2S GRADIENTS (Southern Inceptisol) ===")
    
    # Model 2: Stratified Anoxic-Interface Model
    # We test h = 100 cm (1.0m) and 150 cm (1.5m)
    for model_name, J_0, D_z, h_m in [
        ('Stagnant Bottom Layer (h = 100 cm, Low Flux)', h2s_flux_low, 2.0e-5 * 1e-4 * 86400, 1.0),
        ('Stagnant Bottom Layer (h = 100 cm, High Flux)', h2s_flux_high, 2.0e-5 * 1e-4 * 86400, 1.0),
        ('Stagnant Deep Layer (h = 150 cm, High Flux)', h2s_flux_high, 2.0e-5 * 1e-4 * 86400, 1.5),
        ('Mixed Bottom Layer (h = 100 cm, High Flux)', h2s_flux_high, 2.0e-4 * 1e-4 * 86400, 1.0)
    ]:
        C_0 = (J_0 * h_m) / D_z / 1000.0 # mg/L
        h_cm = h_m * 100.0
        
        print(f"\n--- {model_name} ---")
        print(f"  Sediment-Water Interface C_0: {C_0:.3f} mg/L, Gradient slope: {C_0/h_cm:.5f} mg/L/cm")
        for z_cm in [10, 30, 50, 100, 150]:
            if z_cm <= h_cm:
                c_z = C_0 * (1.0 - z_cm / h_cm)
            else:
                c_z = 0.0
            print(f"  At {z_cm} cm: {c_z:.4f} mg/L")
            
        # Safety distances
        # C(z) = C_0 * (1 - z/h) => z = h * (1 - C_limit/C_0)
        z_avd = h_cm * (1.0 - thr_h2s_avoid / C_0) if C_0 > thr_h2s_avoid else 0
        z_act = h_cm * (1.0 - thr_h2s_acute / C_0) if C_0 > thr_h2s_acute else 0
        print(f"  Safety Distance (Avoidance, 0.002 mg/L): {z_avd:.2f} cm")
        print(f"  Safety Distance (Acute, 0.05 mg/L): {z_act:.2f} cm")

if __name__ == '__main__':
    simulate_refined()
