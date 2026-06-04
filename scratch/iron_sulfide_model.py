import numpy as np

def simulate_gradients():
    # Helper to calculate concentration profile C(z) = C_0 * exp(-z / lambda)
    # Flux J_0 = D_z * C_0 / lambda  =>  C_0 = J_0 * lambda / D_z
    # lambda = sqrt(D_z / k_x)
    # So C(z) = (J_0 / sqrt(D_z * k_x)) * exp(-z * sqrt(k_x / D_z))
    
    # 1. Fe2+ vertical gradient (Northern Ultisol water)
    # Baseline Flux J_0 range: 10 - 50 mmol/m^2/day
    # 1 mmol Fe = 55.85 mg
    # D_z (stagnant bottom boundary layer): we can vary it to see safety distance.
    # Let's test a stagnant case and a slightly mixed case.
    # Stagnant: D_z = 2.0e-5 cm^2/s = 1.728e-1 m^2/day
    # Mixed: D_z = 2.0e-4 cm^2/s = 1.728 m^2/day
    
    fe_flux_low = 10.0 * 55.85 # mg/m^2/day (Zone-B, 5月下旬首觸, low-end)
    fe_flux_high = 50.0 * 55.85 # mg/m^2/day (Zone-A, 6月中旬, high-end)
    
    # Oxidation rate k_x (day^-1): Fe2+ oxidation is slow under low oxygen and acid pH.
    # Zone-A (pH 5.5, high DOC): k_x = 0.12 day^-1 (half-life 5.8 days)
    # Zone-B (pH 6.2, med DOC): k_x = 0.28 day^-1 (half-life 2.5 days)
    
    print("=== Fe2+ Gradient and Safety Distance (Northern) ===")
    
    # We will test D_z = 1.0e-4 cm^2/s = 0.864 m^2/day for stagnant boundary layer
    D_z_fe = 1.0e-4 * 1e-4 * 86400 # m^2/day = 0.864 m^2/day
    k_fe_A = 0.12 # day^-1
    k_fe_B = 0.28 # day^-1
    
    # Thresholds: gill damage = 0.35 mg/L, avoidance = 0.10 mg/L
    thr_damage = 0.35
    thr_avoid = 0.10
    
    for name, J_0, k_x in [('Zone-B (5月下旬, low flux)', fe_flux_low, k_fe_B),
                           ('Zone-A (6月中旬, high flux)', fe_flux_high, k_fe_A)]:
        # Calculate lambda (m)
        lam = np.sqrt(D_z_fe / k_x)
        # C_0 in mg/m^3
        C_0_mg_m3 = (J_0 * lam) / D_z_fe
        C_0 = C_0_mg_m3 / 1000.0 # mg/L
        
        print(f"\n--- {name} ---")
        print(f"Flux J_0: {J_0/55.85:.1f} mmol/m^2/day ({J_0:.1f} mg/m^2/day)")
        print(f"Decay constant k_x: {k_x:.2f} day^-1, Characteristic length lambda: {lam*100:.1f} cm")
        print(f"Sediment-Water Interface C_0: {C_0:.3f} mg/L")
        
        # Concentrations at specific heights (z in cm)
        for z_cm in [10.0, 30.0, 50.0, 100.0]:
            c_z = C_0 * np.exp(-z_cm / (lam * 100.0))
            print(f"  At {z_cm:.0f} cm: {c_z:.3f} mg/L")
            
        # Calculate safety distances
        # z = -lambda * ln(C_limit / C_0)
        if C_0 > thr_damage:
            z_dmg = -lam * 100.0 * np.log(thr_damage / C_0)
            print(f"  Safety Distance (Gill Damage, 0.35 mg/L): {z_dmg:.1f} cm")
        else:
            print(f"  Safety Distance (Gill Damage, 0.35 mg/L): 0 cm (C_0 is {C_0:.3f} mg/L)")
            
        if C_0 > thr_avoid:
            z_avd = -lam * 100.0 * np.log(thr_avoid / C_0)
            print(f"  Safety Distance (Avoidance, 0.10 mg/L): {z_avd:.1f} cm")
        else:
            print(f"  Safety Distance (Avoidance, 0.10 mg/L): 0 cm (C_0 is {C_0:.3f} mg/L)")


    # 2. H2S vertical gradient (Southern Inceptisol water)
    # Flux J_0 range: 19 - 281 mmol/m^2/day
    # 1 mmol H2S = 34.08 mg
    h2s_flux_low = 19.0 * 34.08 # mg/m^2/day (Zone-C, low-end)
    h2s_flux_high = 281.0 * 34.08 # mg/m^2/day (Zone-C, high-end, extreme summer)
    
    # H2S molecular diffusion at 25C and 35C:
    # 25C: D_0 = 1.91e-5 cm^2/s = 0.165 m^2/day
    # 35C: D_0 = 2.32e-5 cm^2/s = 0.200 m^2/day
    # Under stagnant (stoppage): D_z is molecular diffusion.
    # Under slight disturbance (waterwheel on): D_z = 2.0e-4 cm^2/s = 1.728 m^2/day
    
    # Decay constant k_x: H2S chemical/biological oxidation is faster than Fe2+
    # Under low oxygen bottom, let's say k_x = 4.8 day^-1 (half-life 3.5 hr) at 25C
    # At 35C, microbial activity is higher, Q10 = 2.4, so k_x = 4.8 * 2.4 = 11.52 day^-1
    
    print("\n=== H2S Gradient and Safety Distance (Southern) ===")
    
    thr_h2s_avoid = 0.002 # mg/L (behavioral avoidance threshold)
    thr_h2s_acute = 0.05 # mg/L (acute toxicity threshold)
    
    conditions = [
        ('Stagnant, 25°C, Low Flux', h2s_flux_low, 1.91e-5 * 1e-4 * 86400, 4.8),
        ('Stagnant, 35°C, High Flux (Extreme)', h2s_flux_high, 2.32e-5 * 1e-4 * 86400, 11.5),
        ('Slight Disturbance, 25°C, Low Flux', h2s_flux_low, 2.0e-4 * 1e-4 * 86400, 4.8),
        ('Slight Disturbance, 35°C, High Flux', h2s_flux_high, 2.0e-4 * 1e-4 * 86400, 11.5)
    ]
    
    for cond_name, J_0, D_z, k_x in conditions:
        lam = np.sqrt(D_z / k_x)
        C_0_mg_m3 = (J_0 * lam) / D_z
        C_0 = C_0_mg_m3 / 1000.0 # mg/L
        
        print(f"\n--- {cond_name} ---")
        print(f"Flux J_0: {J_0/34.08:.1f} mmol/m^2/day ({J_0:.1f} mg/m^2/day)")
        print(f"Eddy diffusion D_z: {D_z:.4f} m^2/day, Decay constant k_x: {k_x:.2f} day^-1, lambda: {lam*100:.1f} cm")
        print(f"Sediment-Water Interface C_0: {C_0:.4f} mg/L")
        
        # Concentrations at specific heights
        for z_cm in [10.0, 30.0, 50.0, 100.0, 150.0]:
            c_z = C_0 * np.exp(-z_cm / (lam * 100.0))
            print(f"  At {z_cm:.0f} cm: {c_z:.4f} mg/L")
            
        # Safety distances
        if C_0 > thr_h2s_avoid:
            z_avd = -lam * 100.0 * np.log(thr_h2s_avoid / C_0)
            print(f"  Safety Distance (Avoidance, 0.002 mg/L): {z_avd:.1f} cm")
        else:
            print(f"  Safety Distance (Avoidance, 0.002 mg/L): 0 cm")
            
        if C_0 > thr_h2s_acute:
            z_act = -lam * 100.0 * np.log(thr_h2s_acute / C_0)
            print(f"  Safety Distance (Acute, 0.05 mg/L): {z_act:.1f} cm")
        else:
            print(f"  Safety Distance (Acute, 0.05 mg/L): 0 cm")

if __name__ == '__main__':
    simulate_gradients()
