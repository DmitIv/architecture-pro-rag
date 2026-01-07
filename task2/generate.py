#! /usr/bin/env python3
# Generate 30 interconnected fictional facts within one universe as separate Markdown files

import os
import textwrap

base_dir = "./facts"
os.makedirs(base_dir, exist_ok=True)
universe = "The Aurelian Continuum"

facts = [
("""# Fact 01: The Birth of the Aurelian Continuum
The Aurelian Continuum did not originate from an explosion or natural cosmological event. It emerged when an ancient meta-civilization attempted to catalogue every possible state of existence using a universal classification system. When the system exceeded finite representation, the overflow manifested as a self-sustaining reality. This failure became known as the Primary Desynchronization, a reference point repeatedly cited in later temporal studies (see Fact 07 and Fact 19)."""),

("""# Fact 02: The Enumerators
The creators of the original catalog were known as the Enumerators. They were not a species, but a protocol—an ideology of perfect classification implemented across biological minds and machine substrates. Identity among the Enumerators was defined solely by adherence to the protocol. Their disappearance left behind fragments of logic still embedded in artifacts across the Continuum, many of which continue to destabilize local reality (see Fact 11 and Fact 25)."""),

("""# Fact 03: Aurelian Time
Time in the Aurelian Continuum is not linear but conditional. Local regions negotiate temporal flow based on stability, observation, and narrative coherence. This explains how certain individuals appear across centuries without aging. Attempts to impose universal chronology consistently result in structural failure, most notably Temporal Erosion (see Fact 19)."""),

("""# Fact 04: The Lattice Cities
The Lattice Cities are metropolitan constructs existing in overlapping causal phases. Each city occupies the same spatial coordinates but different versions of cause-and-effect. Travel between phases is handled bureaucratically rather than physically. Synchronization failures in the Lattice Cities directly preceded the Civic Silence (see Fact 05)."""),

("""# Fact 05: The Civic Silence
For forty-three years, the Lattice Cities emitted no signals, records, or evidence of activity. Despite this, post-Silence analysis suggests governance and daily life continued uninterrupted. The leading hypothesis is that the cities temporarily exited consensual reality, a concept later formalized in Fact 17."""),

("""# Fact 06: Reality Weights
Every object, person, and event in the Continuum possesses a measurable reality weight. High-weight entities resist alteration, while low-weight ones are susceptible to retroactive change. Reality weights became a core metric during the Accord of Revisions (see Fact 10) and are tracked through the Weight Census (see Fact 18)."""),

("""# Fact 07: The Primary Desynchronization
The Primary Desynchronization marks the moment the Continuum diverged from internal consistency. It is not fixed in time, but expands slowly as an instability front. Temporal loops, duplicated individuals, and causal echoes all trace back to this phenomenon, which underlies most Continuum anomalies."""),

("""# Fact 08: The Mnemonic Seas
The Mnemonic Seas are vast liquid reservoirs of encoded memory. Sailors navigating them often acquire memories belonging to historical figures. Prolonged exposure leads to identity diffusion, a condition central to the case of Navigator Hale (see Fact 14)."""),

("""# Fact 09: The Archive Moons
Orbiting several core worlds are the Archive Moons, artificial satellites containing contradictory historical records. Each moon preserves a different version of events. Modern historians reconstruct consensus history statistically, a practice adopted after the loss of Enumerator authority (see Fact 02)."""),

("""# Fact 10: The Accord of Revisions
The Accord of Revisions legalized controlled alterations to low-weight historical events. Initially successful, the Accord collapsed when revisions began propagating beyond their target scope. These failures eventually produced Autonomous Revisions (see Fact 23)."""),

("""# Fact 11: Paradox Engines
Paradox Engines stabilize reality by continuously generating minor contradictions. Most are powered by degraded Enumerator logic. When miscalibrated, they invert causality, as seen in the creation of the City of Folded Hours (see Fact 15)."""),

("""# Fact 12: The Seventh Survey
The Seventh Survey was launched to locate the Lattice Cities after the Civic Silence. Survey logs indicate successful contact, yet no physical evidence was recovered. This discrepancy remains central to debates about the limits of consensual reality (see Fact 17)."""),

("""# Fact 13: Continuum Fauna
Many native lifeforms of the Continuum exhibit narrative awareness. They alter behavior in response to expectation rather than stimulus. This phenomenon raised ethical concerns formalized in the Ethics of Observation (see Fact 22)."""),

("""# Fact 14: Navigator Hale
Navigator Hale appears in records across multiple centuries, sometimes simultaneously. Scholars debate whether Hale is a single individual affected by temporal recursion (see Fact 03) or a composite identity formed through mnemonic saturation in the Mnemonic Seas (see Fact 08)."""),

("""# Fact 15: The City of Folded Hours
The City of Folded Hours exists within a localized temporal knot. Residents experience full lifetimes while external observers measure minutes. Its creation is directly linked to a Paradox Engine failure (see Fact 11)."""),

("""# Fact 16: Reality Revisions
Reality Revisions are formal procedures for correcting inconsistencies in low-weight history. Although regulated under the Accord of Revisions (see Fact 10), unauthorized revisions persist and contribute to Desynchronization expansion (see Fact 07)."""),

("""# Fact 17: The Consensual Boundary
The Consensual Boundary defines the threshold at which shared belief stabilizes reality. Beyond it, phenomena persist without observers. Crossing this boundary without preparation often results in cognitive fragmentation, as documented by the Seventh Survey (see Fact 12)."""),

("""# Fact 18: The Weight Census
The Weight Census is a recurring measurement of reality weights across the Continuum. Results indicate a gradual decline in average weight, implying increasing malleability of existence and motivating Containment Doctrines (see Fact 24)."""),

("""# Fact 19: Temporal Erosion
Temporal Erosion is the collapse of detailed causality into vague historical summaries. It accelerates near the Primary Desynchronization zone (see Fact 07) and renders precise chronology impossible."""),

("""# Fact 20: The Silent Administrators
The Silent Administrators govern infrastructure without issuing commands. Their existence is inferred solely from system coherence. Many believe they are emergent successors to the Enumerators (see Fact 02)."""),

("""# Fact 21: The Remnant Stations
Remnant Stations are immobile constructs found beyond the Consensual Boundary. They show evidence of long-term habitation, yet no inhabitants have ever been located. Artifacts recovered match descriptions from the Seventh Survey (see Fact 12)."""),

("""# Fact 22: Ethics of Observation
Because observation alters outcomes for narrative-aware entities (see Fact 13), strict non-observation protocols exist. Violations are suspected to have triggered early Civic Silence precursors (see Fact 05)."""),

("""# Fact 23: Autonomous Revisions
Autonomous Revisions are self-propagating historical changes no longer tied to an initiating action. Most originate from failed Accord interventions (see Fact 10) and often manifest as entities or persistent myths."""),

("""# Fact 24: Containment Doctrines
Containment Doctrines prioritize stabilization of high-weight anchors over broad corrections. They emerged in response to Weight Census findings (see Fact 18) but remain politically contested (see Fact 26)."""),

("""# Fact 25: High-Weight Anchors
High-Weight Anchors are entities or locations nearly immune to alteration. They serve as reference points for reconstructing lost history. Many are suspected remnants of Enumerator infrastructure (see Fact 02)."""),

("""# Fact 26: The Doctrinal Schism
The Doctrinal Schism split authorities into interventionist and preservationist factions. Each accuses the other of accelerating erosion. This conflict has stalled coordinated response efforts (see Fact 24)."""),

("""# Fact 27: Narrative Drift
Narrative Drift describes divergence between recorded history and lived experience. Affected individuals recall incompatible pasts. Drift rate correlates strongly with declining reality weights (see Fact 06)."""),

("""# Fact 28: The Last Catalog
The Last Catalog is a partial reconstruction of the original Enumerator system. Attempts to complete it fail catastrophically. Fragments remain essential for Paradox Engine calibration (see Fact 11)."""),

("""# Fact 29: Collapse Scenarios
Collapse Scenarios model possible endpoints of the Continuum. Most predict fragmentation into incompatible realities rather than destruction. These models rely heavily on Weight Census data (see Fact 18)."""),

(f"""# Fact 30: The Open Question
The Open Question asks whether the {universe} can ever return to self-consistency. No model provides a definitive answer. Some theories suggest stabilization requires external observation, a proposal that raises unresolved ethical concerns (see Fact 22).""")
]

paths = []
for i, content in enumerate(facts, 1):
    path = os.path.join(base_dir, f"aurelian_fact_{i:02d}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(textwrap.dedent(content).strip() + "\n")
    paths.append(path)

print(paths)
