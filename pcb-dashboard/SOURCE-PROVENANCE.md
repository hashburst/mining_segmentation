# Source provenance

La baseline del front-end v3.2.5 è HashBurst DePIN TEP-MINER PoC v3.2.4.

SHA-256 del file `index.html` della baseline v3.2.4:

```text
47612c2a694e0d8d8ce8c08419143f8eb182c4251986fc7084845c289aad0cd6
```

SHA-256 del file `server-b/index.html` della versione v3.2.5:

```text
6bed070b47386997bb6c67c3eb7f1f3252beb39206905c87d16382f26a06c013
```

La versione v3.2.4 modificava esclusivamente il dashboard. Il verifier v3.2.3 e la baseline persistente dell'esperimento restavano invariati.

Il repository non include una copia del verifier o di `pcb_emulator.py` quando non è disponibile una corrispondenza certa con i file effettivamente utilizzati dalla generazione runtime v3.2.3 e v3.2.4. Questa scelta evita di attribuire alla versione corrente componenti appartenenti a revisioni differenti.
