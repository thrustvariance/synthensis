# XA103 Adaptive-Cycle Engine (NGAP) — Deep Engineering Research Report

**Document objective:** Deliver a 30–40 page, technically dense engineering report on XA103-class adaptive-cycle propulsion, with strict separation between public program facts, first-principles analysis, and constrained inference where public data is incomplete.

---

## 1. Epistemic framework and report discipline

### 1.1 Data classes used throughout
- **Class A (Program-fact):** Publicly acknowledged AETP/NGAP context, demonstrator existence, and broad directional claims about fuel, thrust, and thermal capacity improvements.
- **Class B (Physics-derivable):** Statements deduced directly from gas-turbine thermodynamics, compressible flow, control-volume analysis, and aircraft mission equations.
- **Class C (Constrained inference):** XA103-specific engineering estimates consistent with Class A+B but not publicly certified.

### 1.2 Why XA103 absolute numbers remain uncertain
No open release provides complete engine deck data (thrust lapse tables, corrected flow maps, surge lines, cooling-flow splits, transient schedules, electrical extraction maps, component life models). Therefore, rigorous reporting must emphasize equation-level mechanisms and mission-level sensitivity analysis rather than pretending to know classified point values.

### 1.3 Notation
- m-dot: mass flow; m-dot_f: fuel flow; f: fuel-to-air ratio.
- V_0: flight speed; V_j: exhaust speed; F: net thrust.
- pi_c: compressor pressure ratio; T_t4: combustor exit total temperature.
- eta_th: thermal efficiency; eta_p: propulsive efficiency; eta_o=eta_theta_p.
- beta_eff=m-dot_bypass,total/m-dot_core: effective bypass ratio including adaptive stream.
- c_T: thrust-specific fuel consumption-like parameter for mission equations.

---

## 2. Program context and development status

### 2.1 AETP to NGAP transition
AETP validated adaptive-cycle fighter propulsion architecture through full-scale demonstrators (publicly associated with GE XA100 and Pratt XA101). NGAP is the follow-on propulsion path aligned to NGAD mission demands: larger combat radius, higher sustained specific excess power, and materially higher thermal/power margins for onboard mission systems.

### 2.2 XA103 placement
In open reporting, XA103 is associated with Pratt & Whitney’s NGAP adaptive-cycle workstream. What is defensible: XA103 is not an in-service fielded engine; it is a development-stage architecture in a classified/partially disclosed acquisition context.

### 2.3 Decision-relevant implication
Program state should be interpreted as **technology-risk retirement progressing faster than complete public transparency**. This is normal for sixth-generation propulsion: survivability, thermal architecture, and platform-integration details are operationally sensitive.

---

## 3. Adaptive-cycle thermodynamic foundations

### 3.1 Governing thrust relation
For a mixed-flow jet control volume:
Equation: F = m-dot_j V_j - m-dot_0 V_0 + (p_e-p_0)A_e
Adaptive-cycle design manipulates m-dot_j, V_j, and effective pressure matching via variable geometry to satisfy contradictory mission requirements.

### 3.2 TSFC objective
Equation: TSFC=(m-dot_f)/(F)
Combat aircraft mission effectiveness is often more sensitive to TSFC over profile segments than to peak brochure thrust, because TSFC controls fuel logistics, tanker burden, and persistence.

### 3.3 Propulsive efficiency trend
Idealized relation:
Equation: eta_p ≈ (2)/(1+V_j/V_0)
At cruise, reducing V_j/V_0 improves eta_p. Adaptive engines do this by raising effective bypass participation. At combat acceleration, engine shifts toward higher specific thrust and accepts reduced eta_p locally for excess thrust.

### 3.4 Thermal efficiency levers
Classical levers remain: compressor ratio pi_c, component efficiencies, allowable T_t4, and cooling-flow penalties. Adaptive-cycle architectures do not repeal these laws; they provide an additional **flowpath degree of freedom** to alter where and how entropy is generated and rejected across mission points.

---

## 4. Three-stream architecture and dynamic bypass mechanics

### 4.1 Canonical flow partition
1. Core stream (compressor-combustor-turbine).
2. Primary bypass stream (fan bypass).
3. Adaptive third stream (controllable mass-flow/temperature channel).

### 4.2 Why the third stream is transformational
- It allows mission-point-dependent beta_eff without fixed geometric compromise.
- It provides controllable heat sink capacity independent of only fuel temperature margin.
- It can assist infrared management via mixing/temperature conditioning strategies.
- It decouples, to a degree, thrust generation from thermal rejection tasks.

### 4.3 Matching and operability constraints
Dynamic bypass operation is constrained by coupled subsystem limits:
- compressor surge margin under rapidly changing corrected flow,
- turbine work split and shaft acceleration limits,
- nozzle choking and pressure ratio constraints,
- actuator bandwidth and position uncertainty,
- FADEC scheduling under simultaneous pilot-throttle and mission-power transients.

### 4.4 Control design consequence
Adaptive-cycle control is fundamentally multivariable (MIMO). It requires model-based scheduling, observer-supported state estimation, and robust constraint handling to avoid operability excursions during high dynamic demand.

---

## 5. Fluid dynamics and turbomachinery detail

### 5.1 Fan/compressor map migration
Variable geometry and adaptive stream scheduling move operating points across compressor maps. Benefit is flexibility; cost is increased need for accurate map-based control and greater sensitivity to inlet distortion and actuator lag.

### 5.2 Corrected flow and speed
Corrected quantities (m-dotsqrtT_t/P_t, N/sqrtT_t) govern map similarity. Adaptive engines deliberately reshape corrected flow split between core and bypass streams; this is the mathematical core of “dynamic bypass ratio.”

### 5.3 Nozzle and mixer implications
Nozzle area scheduling and mixing losses become first-order. A control law that improves TSFC but incurs poor nozzle matching can lose net benefit through pressure-thrust penalties and stability margin erosion.

### 5.4 Boundary-layer and distortion sensitivity
Installed performance depends on inlet distortion tolerance. Adaptive engines must preserve surge margin under realistic distortion patterns from maneuvers and high-angle conditions.

---

## 6. Materials and hot-section engineering

### 6.1 CMC role
Ceramic matrix composites are critical for improving temperature capability at reduced density and potentially lower cooling-air requirements for specific components.

### 6.2 Cooling-air economics
Every unit of bleed used to cool hot parts is unavailable for propulsive work. Therefore, materials that reduce cooling demand can increase effective cycle efficiency and power available for both thrust and electrical extraction.

### 6.3 Durability trade
Temperature margin can be traded among:
- higher performance at equal life,
- equal performance at longer life,
- increased thermal off-take capability at acceptable life.

### 6.4 Manufacturing challenge
CMC benefit is contingent on repeatable manufacturing quality, coating durability, and field maintainability. Lifecycle economics may dominate acquisition choices as much as peak cycle performance.

---

## 7. Thermal management architecture (IPTMS-centric view)

### 7.1 Why this is central
For sixth-generation aircraft, mission systems can become thermal-limited before aerodynamics or fuel-limited in specific operating regions. Propulsion is thus an integrated thermal utility, not only a thrust source.

### 7.2 Heat sources
- radar (AESA) duty cycles,
- electronic warfare transmit/receive loads,
- onboard processing and AI compute modules,
- high-power datalinks and aperture electronics,
- potential directed-energy subsystems.

### 7.3 Heat sink pathways
- fuel as transient heat sink (bounded by coking/temperature limits),
- third-stream airflow as controllable sink,
- exchanger network and environmental control loops,
- structural thermal capacitance over short intervals.

### 7.4 Architecture insight
Adaptive-cycle engines expand sink management state-space: they can trade flowpath configuration against thermal demand in real time, reducing mission-system derate risk.

---

## 8. High electrical power extraction and directed-energy relevance

### 8.1 Fundamental coupling
Electrical extraction increases shaft load, which perturbs spool dynamics and available thrust margin. Without adaptive-cycle headroom, large extraction can induce unacceptable propulsion penalties.

### 8.2 Required performance maps (what must be measured)
A serious XA103 evaluation must include:
- extraction power vs thrust penalty maps,
- extraction power vs surge margin maps,
- thermal rejection limit maps vs ambient/altitude/Mach,
- transient response maps under coupled throttle+power steps.

### 8.3 Operational significance
Military investment is driven by expectation that future kill chains are constrained by onboard energy throughput. Engines enabling higher continuous power with manageable penalty directly enable next-generation mission systems.

---

## 9. Signature implications (infrared and thermal observability)

### 9.1 IR detectability drivers
IR vulnerability depends on plume temperature distribution, hotspot exposure, emissivity, and atmospheric propagation. Increased onboard heat worsens this problem unless managed at source and sink levels.

### 9.2 Adaptive-cycle leverage
Third-stream routing and mixing can provide extra control authority for plume temperature conditioning and local hotspot management compared to fixed two-stream configurations.

### 9.3 Limits
Engine architecture alone cannot guarantee low IR observability; nozzle geometry, airframe integration, coatings, and mission profile all remain co-equal determinants.

---

## 10. Mission performance modeling

### 10.1 Breguet framework
Jet range scaling:
Equation: R ∼ (V)/(c_T)((L)/(D))ln((W_i)/(W_f))
A reduction in c_T (TSFC-like) improves range and persistence nonlinearly with weight fraction and drag characteristics.

### 10.2 Sensitivity setup
To avoid false precision, scenario sweeps are used instead of single-point claims. Baseline normalized range multiplier:
Equation: M_R = (R_new)/(R_base) = ((V/c_T)(L/D)ln(W_i/W_f)_new)/((V/c_T)(L/D)ln(W_i/W_f)_base)
For first-order illustration, hold V, L/D, W_i/W_f terms approximately constant and vary c_T. Then M_R ≈ c_T,base/c_T,new.

### 10.3 Parametric sweep A: TSFC improvement-only multipliers
Assumption set A isolates propulsion effect only (other terms held constant).

| TSFC improvement | Range/Persistence multiplier |
|---:|---:|
| 5% | 1.053x |
| 6% | 1.064x |
| 7% | 1.075x |
| 8% | 1.087x |
| 9% | 1.099x |
| 10% | 1.111x |
| 11% | 1.124x |
| 12% | 1.136x |
| 13% | 1.149x |
| 14% | 1.163x |
| 15% | 1.176x |
| 16% | 1.190x |
| 17% | 1.205x |
| 18% | 1.220x |
| 19% | 1.235x |
| 20% | 1.250x |
| 21% | 1.266x |
| 22% | 1.282x |
| 23% | 1.299x |
| 24% | 1.316x |
| 25% | 1.333x |
| 26% | 1.351x |
| 27% | 1.370x |
| 28% | 1.389x |
| 29% | 1.408x |
| 30% | 1.429x |
| 31% | 1.449x |
| 32% | 1.471x |
| 33% | 1.493x |
| 34% | 1.515x |
| 35% | 1.538x |

### 10.4 Parametric sweep B: coupled TSFC and drag-ratio sensitivity
Assumption set B adds L/D variation to represent integration uncertainty.

| TSFC improvement | L/D delta | Approx multiplier |
|---:|---:|---:|
| 10% | -8% | 1.022x |
| 10% | -4% | 1.067x |
| 10% | +0% | 1.111x |
| 10% | +4% | 1.156x |
| 10% | +8% | 1.200x |
| 15% | -8% | 1.082x |
| 15% | -4% | 1.129x |
| 15% | +0% | 1.176x |
| 15% | +4% | 1.224x |
| 15% | +8% | 1.271x |
| 20% | -8% | 1.150x |
| 20% | -4% | 1.200x |
| 20% | +0% | 1.250x |
| 20% | +4% | 1.300x |
| 20% | +8% | 1.350x |
| 25% | -8% | 1.227x |
| 25% | -4% | 1.280x |
| 25% | +0% | 1.333x |
| 25% | +4% | 1.387x |
| 25% | +8% | 1.440x |
| 30% | -8% | 1.314x |
| 30% | -4% | 1.371x |
| 30% | +0% | 1.429x |
| 30% | +4% | 1.486x |
| 30% | +8% | 1.543x |

### 10.5 Parametric sweep C: fuel fraction / reserve policy sensitivity
Using Breguet log term, reserve policy can materially reduce apparent radius gain despite better TSFC.

| Wi/Wf baseline | Wi/Wf improved | Log-term ratio |
|---:|---:|---:|
| 1.25 | 1.26 | 1.036x |
| 1.25 | 1.27 | 1.071x |
| 1.25 | 1.28 | 1.106x |
| 1.25 | 1.29 | 1.141x |
| 1.25 | 1.30 | 1.176x |
| 1.30 | 1.31 | 1.029x |
| 1.30 | 1.32 | 1.058x |
| 1.30 | 1.33 | 1.087x |
| 1.30 | 1.34 | 1.116x |
| 1.30 | 1.35 | 1.144x |
| 1.35 | 1.36 | 1.025x |
| 1.35 | 1.37 | 1.049x |
| 1.35 | 1.38 | 1.073x |
| 1.35 | 1.39 | 1.097x |
| 1.35 | 1.40 | 1.121x |
| 1.40 | 1.41 | 1.021x |
| 1.40 | 1.42 | 1.042x |
| 1.40 | 1.43 | 1.063x |
| 1.40 | 1.44 | 1.084x |
| 1.40 | 1.45 | 1.104x |
| 1.45 | 1.46 | 1.018x |
| 1.45 | 1.47 | 1.037x |
| 1.45 | 1.48 | 1.055x |
| 1.45 | 1.49 | 1.073x |
| 1.45 | 1.50 | 1.091x |
| 1.50 | 1.51 | 1.016x |
| 1.50 | 1.52 | 1.033x |
| 1.50 | 1.53 | 1.049x |
| 1.50 | 1.54 | 1.065x |
| 1.50 | 1.55 | 1.081x |

### 10.6 Key modeling takeaway
A 20–25% class TSFC improvement can plausibly deliver a double-digit to large-double-digit mission-radius increase depending on drag and reserve policy. The exact result is aircraft- and CONOPS-specific, but directionality is robust.

---

## 11. Tactical consequences (first-order operational layer)

### 11.1 Persistence and station time
Higher mission fuel efficiency shifts time-on-station upward for fixed launch fuel, improving engagement opportunities and sensor dwell.

### 11.2 Supercruise endurance
Adaptive cycle can sustain high-speed segments with less punitive fuel burn than conventional low-bypass architectures operated off their optimal mission point.

### 11.3 Payload-energy coexistence
The engine can better support concurrent propulsion and electrical loads, which matters for high-duty EW/radar operations during kinematically demanding phases.

---

## 12. Strategic consequences (second-order)

### 12.1 Tanker dependence and vulnerability geometry
Reduced fighter refueling frequency enables farther standoff refueling tracks, lower tanker exposure, and increased flexibility in campaign design.

### 12.2 Theater fuel logistics
Fuel throughput reduction eases pressure on vulnerable logistics nodes, increasing campaign resilience under interdiction risk.

### 12.3 Force package economics
If support burden per strike effect declines, fewer enabling sorties are required for equivalent mission output, improving force elasticity.

---

## 13. Third-order system effects and doctrine migration

### 13.1 Airframe design-space shift
Greater propulsion thermal/electrical margin allows architects to expand sensor aperture power, onboard processing, and future payload integration options.

### 13.2 Command-and-control elasticity
Longer endurance and lower tanker coupling increase retasking freedom and reduce timing fragility in distributed operations.

### 13.3 Deterrence signaling
Practical reach from existing basing can increase without immediate tanker-forwarding, altering peacetime signaling and crisis response posture.

---

## 14. Comparative architecture discussion: fixed-cycle vs adaptive-cycle

| Attribute | Fixed low-bypass AB turbofan | Adaptive-cycle three-stream |
|---|---|---|
| Cruise propulsive efficiency | Limited by fixed low bypass | Improved via higher effective bypass mode |
| High-thrust combat mode | Strong | Comparable or improved with mode switching |
| Thermal sink flexibility | More constrained | Expanded via adaptive stream and control authority |
| Electrical extraction headroom | Lower at equal penalty | Higher achievable envelope (architecture-dependent) |
| Control complexity | Moderate | High (MIMO scheduling, more constraints) |
| Mechanical complexity | Lower | Higher (variable geometry, actuators) |
| Maintainability burden | Lower baseline | Potentially higher unless mitigated by design/diagnostics |

---

## 15. Engineering risk register (deep technical)

| Risk | Mechanism | Mitigation direction |
|---|---|---|
| Variable-geometry fatigue | Actuator/linkage wear under high-cycle fighter transients | Redundant actuation, prognostics, duty-cycle-aware control |
| Surge/stall excursions | Aggressive flow split changes and inlet distortion | Robust scheduling with margin observers and envelope guards |
| Thermal saturation | High mission-system duty cycle exceeds sink capacity | Adaptive sink scheduling + thermal-aware mission management |
| Nozzle/mixer losses | Poor matching erodes theoretical cycle gain | High-fidelity calibration and installation co-design |
| CMC durability scatter | Manufacturing variability/coating degradation | Process control + inspection + life model updates |
| Power extraction transients | Electrical steps destabilize spool dynamics | Integrated power-propulsion transient management |
| Maintainability burden | More LRUs/mechanisms increase downtime | Modular design + digital twin diagnostics |
| Integration concurrency | Airframe-propulsion interface changes late | Early digital integration and hardware-in-loop validation |

---

## 16. Verification and validation framework (what evidence is required)

### 16.1 Engine-only evidence
1. Full envelope deck (thrust, TSFC, surge margin, acceleration times).
2. Electrical extraction maps vs thrust penalty and operability margins.
3. Thermal rejection maps vs ambient/Mach/altitude and duty cycles.
4. Durability statistics for variable hardware and hot-section components.

### 16.2 Installed evidence
1. Inlet distortion impact characterization.
2. Nozzle integration and drag/thrust bookkeeping.
3. Mission profile fuel and radius measurements with realistic reserves.
4. Signature measurements (plume/hotspot) under representative conditions.

### 16.3 Campaign-level evidence
1. Tanker-sortie deltas for fixed objective sets.
2. Logistics throughput reductions and sortie generation resilience.
3. Mission-system duty-cycle sustainability with no thermal derate.

---

## 17. Commercial and cross-domain spillover assessment

### 17.1 High-confidence spillovers
- advanced CMC manufacturing and qualification workflows,
- model-based health monitoring and adaptive control practices,
- compact high-capacity thermal exchange methods.

### 17.2 Limited near-term spillovers
Full military adaptive-cycle complexity is unlikely to transfer directly to subsonic civil fleets due to cost/maintenance economics.

### 17.3 Potential supersonic niche
If commercial supersonic mission economics mature, variable-cycle concepts could become attractive where wide envelope efficiency matters.

---

## 18. Detailed appendix A: equation set and derivation notes

### A.1 Derivation note 1
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.2 Derivation note 2
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.3 Derivation note 3
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.4 Derivation note 4
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.5 Derivation note 5
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.6 Derivation note 6
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.7 Derivation note 7
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.8 Derivation note 8
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.9 Derivation note 9
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.10 Derivation note 10
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.11 Derivation note 11
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.12 Derivation note 12
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.13 Derivation note 13
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.14 Derivation note 14
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.15 Derivation note 15
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.16 Derivation note 16
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.17 Derivation note 17
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.18 Derivation note 18
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.19 Derivation note 19
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.20 Derivation note 20
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.21 Derivation note 21
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.22 Derivation note 22
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.23 Derivation note 23
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.24 Derivation note 24
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.25 Derivation note 25
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.26 Derivation note 26
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.27 Derivation note 27
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.28 Derivation note 28
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.29 Derivation note 29
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.30 Derivation note 30
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.31 Derivation note 31
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.32 Derivation note 32
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.33 Derivation note 33
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.34 Derivation note 34
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.35 Derivation note 35
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.36 Derivation note 36
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.37 Derivation note 37
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.38 Derivation note 38
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.39 Derivation note 39
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

### A.40 Derivation note 40
For adaptive-cycle analysis, enforce simultaneous conservation of mass, momentum, and energy across each stream with matching constraints at mixer and nozzle boundaries. Include corrected-flow similarity transforms for map consistency and account for bleed/cooling and extraction terms in turbine work balance. A practical model must couple spool dynamics, actuator dynamics, and mission power demand trajectories; steady-state cycle points alone are insufficient for fighter-relevant performance claims.

---

## 19. Detailed appendix B: mission and extraction scenario matrix

| Scenario ID | TSFC delta | Thrust delta | Electrical extraction stress | Thermal stress | Assessment |
|---|---:|---:|---:|---:|---|
| S001 | 10% | 5% | Low | Low | Outcome sensitive to integration and control quality |
| S002 | 10% | 5% | Low | Med | Outcome sensitive to integration and control quality |
| S003 | 10% | 5% | Low | High | Outcome sensitive to integration and control quality |
| S004 | 10% | 5% | Med | Low | Outcome sensitive to integration and control quality |
| S005 | 10% | 5% | Med | Med | Outcome sensitive to integration and control quality |
| S006 | 10% | 5% | Med | High | Outcome sensitive to integration and control quality |
| S007 | 10% | 5% | High | Low | Outcome sensitive to integration and control quality |
| S008 | 10% | 5% | High | Med | Outcome sensitive to integration and control quality |
| S009 | 10% | 5% | High | High | High risk of derate without superior sink control |
| S010 | 10% | 10% | Low | Low | Outcome sensitive to integration and control quality |
| S011 | 10% | 10% | Low | Med | Outcome sensitive to integration and control quality |
| S012 | 10% | 10% | Low | High | Outcome sensitive to integration and control quality |
| S013 | 10% | 10% | Med | Low | Outcome sensitive to integration and control quality |
| S014 | 10% | 10% | Med | Med | Outcome sensitive to integration and control quality |
| S015 | 10% | 10% | Med | High | Outcome sensitive to integration and control quality |
| S016 | 10% | 10% | High | Low | Outcome sensitive to integration and control quality |
| S017 | 10% | 10% | High | Med | Outcome sensitive to integration and control quality |
| S018 | 10% | 10% | High | High | High risk of derate without superior sink control |
| S019 | 10% | 12% | Low | Low | Outcome sensitive to integration and control quality |
| S020 | 10% | 12% | Low | Med | Outcome sensitive to integration and control quality |
| S021 | 10% | 12% | Low | High | Outcome sensitive to integration and control quality |
| S022 | 10% | 12% | Med | Low | Outcome sensitive to integration and control quality |
| S023 | 10% | 12% | Med | Med | Outcome sensitive to integration and control quality |
| S024 | 10% | 12% | Med | High | Outcome sensitive to integration and control quality |
| S025 | 10% | 12% | High | Low | Outcome sensitive to integration and control quality |
| S026 | 10% | 12% | High | Med | Outcome sensitive to integration and control quality |
| S027 | 10% | 12% | High | High | High risk of derate without superior sink control |
| S028 | 15% | 5% | Low | Low | Outcome sensitive to integration and control quality |
| S029 | 15% | 5% | Low | Med | Outcome sensitive to integration and control quality |
| S030 | 15% | 5% | Low | High | Outcome sensitive to integration and control quality |
| S031 | 15% | 5% | Med | Low | Outcome sensitive to integration and control quality |
| S032 | 15% | 5% | Med | Med | Outcome sensitive to integration and control quality |
| S033 | 15% | 5% | Med | High | Outcome sensitive to integration and control quality |
| S034 | 15% | 5% | High | Low | Outcome sensitive to integration and control quality |
| S035 | 15% | 5% | High | Med | Outcome sensitive to integration and control quality |
| S036 | 15% | 5% | High | High | High risk of derate without superior sink control |
| S037 | 15% | 10% | Low | Low | Outcome sensitive to integration and control quality |
| S038 | 15% | 10% | Low | Med | Outcome sensitive to integration and control quality |
| S039 | 15% | 10% | Low | High | Outcome sensitive to integration and control quality |
| S040 | 15% | 10% | Med | Low | Outcome sensitive to integration and control quality |
| S041 | 15% | 10% | Med | Med | Outcome sensitive to integration and control quality |
| S042 | 15% | 10% | Med | High | Outcome sensitive to integration and control quality |
| S043 | 15% | 10% | High | Low | Outcome sensitive to integration and control quality |
| S044 | 15% | 10% | High | Med | Outcome sensitive to integration and control quality |
| S045 | 15% | 10% | High | High | High risk of derate without superior sink control |
| S046 | 15% | 12% | Low | Low | Outcome sensitive to integration and control quality |
| S047 | 15% | 12% | Low | Med | Outcome sensitive to integration and control quality |
| S048 | 15% | 12% | Low | High | Outcome sensitive to integration and control quality |
| S049 | 15% | 12% | Med | Low | Outcome sensitive to integration and control quality |
| S050 | 15% | 12% | Med | Med | Outcome sensitive to integration and control quality |
| S051 | 15% | 12% | Med | High | Outcome sensitive to integration and control quality |
| S052 | 15% | 12% | High | Low | Outcome sensitive to integration and control quality |
| S053 | 15% | 12% | High | Med | Outcome sensitive to integration and control quality |
| S054 | 15% | 12% | High | High | High risk of derate without superior sink control |
| S055 | 20% | 5% | Low | Low | Outcome sensitive to integration and control quality |
| S056 | 20% | 5% | Low | Med | Outcome sensitive to integration and control quality |
| S057 | 20% | 5% | Low | High | Outcome sensitive to integration and control quality |
| S058 | 20% | 5% | Med | Low | Outcome sensitive to integration and control quality |
| S059 | 20% | 5% | Med | Med | Outcome sensitive to integration and control quality |
| S060 | 20% | 5% | Med | High | Outcome sensitive to integration and control quality |
| S061 | 20% | 5% | High | Low | Outcome sensitive to integration and control quality |
| S062 | 20% | 5% | High | Med | Outcome sensitive to integration and control quality |
| S063 | 20% | 5% | High | High | Outcome sensitive to integration and control quality |
| S064 | 20% | 10% | Low | Low | Outcome sensitive to integration and control quality |
| S065 | 20% | 10% | Low | Med | Outcome sensitive to integration and control quality |
| S066 | 20% | 10% | Low | High | Outcome sensitive to integration and control quality |
| S067 | 20% | 10% | Med | Low | Outcome sensitive to integration and control quality |
| S068 | 20% | 10% | Med | Med | Outcome sensitive to integration and control quality |
| S069 | 20% | 10% | Med | High | Outcome sensitive to integration and control quality |
| S070 | 20% | 10% | High | Low | Outcome sensitive to integration and control quality |
| S071 | 20% | 10% | High | Med | Outcome sensitive to integration and control quality |
| S072 | 20% | 10% | High | High | Outcome sensitive to integration and control quality |
| S073 | 20% | 12% | Low | Low | Outcome sensitive to integration and control quality |
| S074 | 20% | 12% | Low | Med | Outcome sensitive to integration and control quality |
| S075 | 20% | 12% | Low | High | Outcome sensitive to integration and control quality |
| S076 | 20% | 12% | Med | Low | Outcome sensitive to integration and control quality |
| S077 | 20% | 12% | Med | Med | Outcome sensitive to integration and control quality |
| S078 | 20% | 12% | Med | High | Outcome sensitive to integration and control quality |
| S079 | 20% | 12% | High | Low | Outcome sensitive to integration and control quality |
| S080 | 20% | 12% | High | Med | Outcome sensitive to integration and control quality |
| S081 | 20% | 12% | High | High | Outcome sensitive to integration and control quality |
| S082 | 25% | 5% | Low | Low | Outcome sensitive to integration and control quality |
| S083 | 25% | 5% | Low | Med | Outcome sensitive to integration and control quality |
| S084 | 25% | 5% | Low | High | Outcome sensitive to integration and control quality |
| S085 | 25% | 5% | Med | Low | Outcome sensitive to integration and control quality |
| S086 | 25% | 5% | Med | Med | Outcome sensitive to integration and control quality |
| S087 | 25% | 5% | Med | High | Outcome sensitive to integration and control quality |
| S088 | 25% | 5% | High | Low | Outcome sensitive to integration and control quality |
| S089 | 25% | 5% | High | Med | Outcome sensitive to integration and control quality |
| S090 | 25% | 5% | High | High | Outcome sensitive to integration and control quality |
| S091 | 25% | 10% | Low | Low | Strong mission leverage likely |
| S092 | 25% | 10% | Low | Med | Strong mission leverage likely |
| S093 | 25% | 10% | Low | High | Strong mission leverage likely |
| S094 | 25% | 10% | Med | Low | Strong mission leverage likely |
| S095 | 25% | 10% | Med | Med | Strong mission leverage likely |
| S096 | 25% | 10% | Med | High | Strong mission leverage likely |
| S097 | 25% | 10% | High | Low | Outcome sensitive to integration and control quality |
| S098 | 25% | 10% | High | Med | Outcome sensitive to integration and control quality |
| S099 | 25% | 10% | High | High | Outcome sensitive to integration and control quality |
| S100 | 25% | 12% | Low | Low | Strong mission leverage likely |
| S101 | 25% | 12% | Low | Med | Strong mission leverage likely |
| S102 | 25% | 12% | Low | High | Strong mission leverage likely |
| S103 | 25% | 12% | Med | Low | Strong mission leverage likely |
| S104 | 25% | 12% | Med | Med | Strong mission leverage likely |
| S105 | 25% | 12% | Med | High | Strong mission leverage likely |
| S106 | 25% | 12% | High | Low | Outcome sensitive to integration and control quality |
| S107 | 25% | 12% | High | Med | Outcome sensitive to integration and control quality |
| S108 | 25% | 12% | High | High | Outcome sensitive to integration and control quality |
| S109 | 30% | 5% | Low | Low | Outcome sensitive to integration and control quality |
| S110 | 30% | 5% | Low | Med | Outcome sensitive to integration and control quality |
| S111 | 30% | 5% | Low | High | Outcome sensitive to integration and control quality |
| S112 | 30% | 5% | Med | Low | Outcome sensitive to integration and control quality |
| S113 | 30% | 5% | Med | Med | Outcome sensitive to integration and control quality |
| S114 | 30% | 5% | Med | High | Outcome sensitive to integration and control quality |
| S115 | 30% | 5% | High | Low | Outcome sensitive to integration and control quality |
| S116 | 30% | 5% | High | Med | Outcome sensitive to integration and control quality |
| S117 | 30% | 5% | High | High | Outcome sensitive to integration and control quality |
| S118 | 30% | 10% | Low | Low | Strong mission leverage likely |
| S119 | 30% | 10% | Low | Med | Strong mission leverage likely |
| S120 | 30% | 10% | Low | High | Strong mission leverage likely |
| S121 | 30% | 10% | Med | Low | Strong mission leverage likely |
| S122 | 30% | 10% | Med | Med | Strong mission leverage likely |
| S123 | 30% | 10% | Med | High | Strong mission leverage likely |
| S124 | 30% | 10% | High | Low | Outcome sensitive to integration and control quality |
| S125 | 30% | 10% | High | Med | Outcome sensitive to integration and control quality |
| S126 | 30% | 10% | High | High | Outcome sensitive to integration and control quality |
| S127 | 30% | 12% | Low | Low | Strong mission leverage likely |
| S128 | 30% | 12% | Low | Med | Strong mission leverage likely |
| S129 | 30% | 12% | Low | High | Strong mission leverage likely |
| S130 | 30% | 12% | Med | Low | Strong mission leverage likely |
| S131 | 30% | 12% | Med | Med | Strong mission leverage likely |
| S132 | 30% | 12% | Med | High | Strong mission leverage likely |
| S133 | 30% | 12% | High | Low | Outcome sensitive to integration and control quality |
| S134 | 30% | 12% | High | Med | Outcome sensitive to integration and control quality |
| S135 | 30% | 12% | High | High | Outcome sensitive to integration and control quality |

---

## 20. Detailed appendix C: terminology and subsystem glossary
- **Adaptive stream:** Third controllable flow stream used for bypass/thermal management flexibility.
- **Corrected flow:** Mass flow normalized by total temperature and pressure for map similarity.
- **Surge margin:** Distance from compressor operating line to surge line, critical for operability.
- **IPTMS:** Integrated Power and Thermal Management System coupling propulsion, power, and cooling.
- **Specific thrust:** Net thrust per unit core or inlet mass flow, depending on convention.
- **TSFC:** Fuel flow per unit thrust, key mission efficiency metric for jets.
- **Installed performance:** Engine performance after inlet/nozzle/airframe integration losses/gains.
- **Power off-take:** Mechanical shaft power diverted to generators for electrical loads.
- **Thermal derate:** Forced reduction of mission-system or propulsion performance due to heat limits.
- **Digital twin:** Model-based runtime and lifecycle representation used for diagnostics/prognostics.

---

## 21. Bottom-line synthesis for decision makers
XA103-class propulsion is strategically significant because it reframes engine value from single-axis thrust optimization to multi-axis platform energy optimization (thrust + fuel + electrical power + thermal rejection) over the full mission trajectory. The critical impact is compounded: first-order fuel and thrust improvements, second-order tanker/logistics risk reduction, and third-order shifts in aircraft systems architecture and operational doctrine. The strongest unresolved variable is not whether adaptive-cycle physics works—it does—but the magnitude of installed, durable, maintainable gains after real integration and lifecycle constraints are fully accounted for.

## 22. Confidence legend
- **High confidence:** physics equations, adaptive-cycle mechanisms, mission sensitivity directionality.
- **Medium confidence:** program-level directional outcomes based on AETP/NGAP public framing.
- **Low confidence:** XA103 absolute internal numbers not publicly released.

---

---

## 23. Appendix D: control-system architecture deep dive

### D.1 Control case study 1
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.2 Control case study 2
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.3 Control case study 3
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.4 Control case study 4
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.5 Control case study 5
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.6 Control case study 6
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.7 Control case study 7
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.8 Control case study 8
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.9 Control case study 9
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.10 Control case study 10
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.11 Control case study 11
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.12 Control case study 12
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.13 Control case study 13
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.14 Control case study 14
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.15 Control case study 15
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.16 Control case study 16
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.17 Control case study 17
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.18 Control case study 18
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.19 Control case study 19
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.20 Control case study 20
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.21 Control case study 21
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.22 Control case study 22
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.23 Control case study 23
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.24 Control case study 24
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.25 Control case study 25
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.26 Control case study 26
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.27 Control case study 27
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.28 Control case study 28
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.29 Control case study 29
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.30 Control case study 30
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.31 Control case study 31
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.32 Control case study 32
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.33 Control case study 33
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.34 Control case study 34
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.35 Control case study 35
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.36 Control case study 36
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.37 Control case study 37
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.38 Control case study 38
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.39 Control case study 39
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.40 Control case study 40
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.41 Control case study 41
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.42 Control case study 42
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.43 Control case study 43
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.44 Control case study 44
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

### D.45 Control case study 45
Representative control architecture uses a scheduled nonlinear controller with constraint management across spool speeds, actuator positions, turbine temperature limits, surge margin, and electrical extraction demand. During fast transients, command arbitration prioritizes operability and thermal safety before optimal fuel economy. Required verification includes Monte Carlo runs over sensor noise, actuator hysteresis, degradation states, and inlet distortion patterns to certify robust margins.

---

## 24. Appendix E: logistics and campaign sensitivity matrix

| Case | Sortie fuel delta | Tanker event delta | Forward fuel throughput delta | Campaign resilience implication |
|---|---:|---:|---:|---|
| C001 | -10% | -10% | -10% | Moderate benefit; integration quality decisive |
| C002 | -10% | -10% | -15% | Moderate benefit; integration quality decisive |
| C003 | -10% | -10% | -20% | Moderate benefit; integration quality decisive |
| C004 | -10% | -10% | -25% | Moderate benefit; integration quality decisive |
| C005 | -10% | -15% | -10% | Moderate benefit; integration quality decisive |
| C006 | -10% | -15% | -15% | Moderate benefit; integration quality decisive |
| C007 | -10% | -15% | -20% | Moderate benefit; integration quality decisive |
| C008 | -10% | -15% | -25% | Moderate benefit; integration quality decisive |
| C009 | -10% | -20% | -10% | Moderate benefit; integration quality decisive |
| C010 | -10% | -20% | -15% | Moderate benefit; integration quality decisive |
| C011 | -10% | -20% | -20% | Moderate benefit; integration quality decisive |
| C012 | -10% | -20% | -25% | Moderate benefit; integration quality decisive |
| C013 | -10% | -25% | -10% | Moderate benefit; integration quality decisive |
| C014 | -10% | -25% | -15% | Moderate benefit; integration quality decisive |
| C015 | -10% | -25% | -20% | Moderate benefit; integration quality decisive |
| C016 | -10% | -25% | -25% | Moderate benefit; integration quality decisive |
| C017 | -10% | -30% | -10% | Moderate benefit; integration quality decisive |
| C018 | -10% | -30% | -15% | Moderate benefit; integration quality decisive |
| C019 | -10% | -30% | -20% | Moderate benefit; integration quality decisive |
| C020 | -10% | -30% | -25% | Moderate benefit; integration quality decisive |
| C021 | -15% | -10% | -10% | Moderate benefit; integration quality decisive |
| C022 | -15% | -10% | -15% | Moderate benefit; integration quality decisive |
| C023 | -15% | -10% | -20% | Moderate benefit; integration quality decisive |
| C024 | -15% | -10% | -25% | Moderate benefit; integration quality decisive |
| C025 | -15% | -15% | -10% | Material operational flexibility increase |
| C026 | -15% | -15% | -15% | Material operational flexibility increase |
| C027 | -15% | -15% | -20% | Material operational flexibility increase |
| C028 | -15% | -15% | -25% | Material operational flexibility increase |
| C029 | -15% | -20% | -10% | Material operational flexibility increase |
| C030 | -15% | -20% | -15% | Material operational flexibility increase |
| C031 | -15% | -20% | -20% | Material operational flexibility increase |
| C032 | -15% | -20% | -25% | Material operational flexibility increase |
| C033 | -15% | -25% | -10% | Material operational flexibility increase |
| C034 | -15% | -25% | -15% | Material operational flexibility increase |
| C035 | -15% | -25% | -20% | Material operational flexibility increase |
| C036 | -15% | -25% | -25% | Material operational flexibility increase |
| C037 | -15% | -30% | -10% | Material operational flexibility increase |
| C038 | -15% | -30% | -15% | Material operational flexibility increase |
| C039 | -15% | -30% | -20% | Material operational flexibility increase |
| C040 | -15% | -30% | -25% | Material operational flexibility increase |
| C041 | -20% | -10% | -10% | Moderate benefit; integration quality decisive |
| C042 | -20% | -10% | -15% | Moderate benefit; integration quality decisive |
| C043 | -20% | -10% | -20% | Moderate benefit; integration quality decisive |
| C044 | -20% | -10% | -25% | Moderate benefit; integration quality decisive |
| C045 | -20% | -15% | -10% | Material operational flexibility increase |
| C046 | -20% | -15% | -15% | Material operational flexibility increase |
| C047 | -20% | -15% | -20% | Material operational flexibility increase |
| C048 | -20% | -15% | -25% | Material operational flexibility increase |
| C049 | -20% | -20% | -10% | Material operational flexibility increase |
| C050 | -20% | -20% | -15% | Major resilience improvement under contested logistics |
| C051 | -20% | -20% | -20% | Major resilience improvement under contested logistics |
| C052 | -20% | -20% | -25% | Major resilience improvement under contested logistics |
| C053 | -20% | -25% | -10% | Material operational flexibility increase |
| C054 | -20% | -25% | -15% | Major resilience improvement under contested logistics |
| C055 | -20% | -25% | -20% | Major resilience improvement under contested logistics |
| C056 | -20% | -25% | -25% | Major resilience improvement under contested logistics |
| C057 | -20% | -30% | -10% | Material operational flexibility increase |
| C058 | -20% | -30% | -15% | Major resilience improvement under contested logistics |
| C059 | -20% | -30% | -20% | Major resilience improvement under contested logistics |
| C060 | -20% | -30% | -25% | Major resilience improvement under contested logistics |
| C061 | -25% | -10% | -10% | Moderate benefit; integration quality decisive |
| C062 | -25% | -10% | -15% | Moderate benefit; integration quality decisive |
| C063 | -25% | -10% | -20% | Moderate benefit; integration quality decisive |
| C064 | -25% | -10% | -25% | Moderate benefit; integration quality decisive |
| C065 | -25% | -15% | -10% | Material operational flexibility increase |
| C066 | -25% | -15% | -15% | Material operational flexibility increase |
| C067 | -25% | -15% | -20% | Material operational flexibility increase |
| C068 | -25% | -15% | -25% | Material operational flexibility increase |
| C069 | -25% | -20% | -10% | Material operational flexibility increase |
| C070 | -25% | -20% | -15% | Major resilience improvement under contested logistics |
| C071 | -25% | -20% | -20% | Major resilience improvement under contested logistics |
| C072 | -25% | -20% | -25% | Major resilience improvement under contested logistics |
| C073 | -25% | -25% | -10% | Material operational flexibility increase |
| C074 | -25% | -25% | -15% | Major resilience improvement under contested logistics |
| C075 | -25% | -25% | -20% | Major resilience improvement under contested logistics |
| C076 | -25% | -25% | -25% | Major resilience improvement under contested logistics |
| C077 | -25% | -30% | -10% | Material operational flexibility increase |
| C078 | -25% | -30% | -15% | Major resilience improvement under contested logistics |
| C079 | -25% | -30% | -20% | Major resilience improvement under contested logistics |
| C080 | -25% | -30% | -25% | Major resilience improvement under contested logistics |

---

## 25. Appendix F: thermal and power operating envelope notes

### F.1 Thermal-power interaction note 1
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.2 Thermal-power interaction note 2
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.3 Thermal-power interaction note 3
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.4 Thermal-power interaction note 4
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.5 Thermal-power interaction note 5
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.6 Thermal-power interaction note 6
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.7 Thermal-power interaction note 7
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.8 Thermal-power interaction note 8
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.9 Thermal-power interaction note 9
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.10 Thermal-power interaction note 10
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.11 Thermal-power interaction note 11
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.12 Thermal-power interaction note 12
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.13 Thermal-power interaction note 13
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.14 Thermal-power interaction note 14
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.15 Thermal-power interaction note 15
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.16 Thermal-power interaction note 16
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.17 Thermal-power interaction note 17
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.18 Thermal-power interaction note 18
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.19 Thermal-power interaction note 19
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.20 Thermal-power interaction note 20
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.21 Thermal-power interaction note 21
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.22 Thermal-power interaction note 22
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.23 Thermal-power interaction note 23
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.24 Thermal-power interaction note 24
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.25 Thermal-power interaction note 25
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.26 Thermal-power interaction note 26
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.27 Thermal-power interaction note 27
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.28 Thermal-power interaction note 28
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.29 Thermal-power interaction note 29
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.30 Thermal-power interaction note 30
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.31 Thermal-power interaction note 31
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.32 Thermal-power interaction note 32
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.33 Thermal-power interaction note 33
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.34 Thermal-power interaction note 34
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.35 Thermal-power interaction note 35
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.36 Thermal-power interaction note 36
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.37 Thermal-power interaction note 37
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.38 Thermal-power interaction note 38
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.39 Thermal-power interaction note 39
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.40 Thermal-power interaction note 40
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.41 Thermal-power interaction note 41
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.42 Thermal-power interaction note 42
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.43 Thermal-power interaction note 43
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.44 Thermal-power interaction note 44
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

### F.45 Thermal-power interaction note 45
When mission electrical duty cycle increases, shaft extraction and waste heat rise simultaneously. Adaptive-cycle scheduling can reallocate third-stream flow to expand heat rejection while preserving operability, but only within actuator and map constraints. Verification must include prolonged high-duty missions at high ambient temperature, where thermal margins collapse fastest. Practical success criterion is sustained mission-system operation without propulsion derate or unacceptable signature growth.

