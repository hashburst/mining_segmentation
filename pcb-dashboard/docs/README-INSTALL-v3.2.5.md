# HashBurst DePIN TEP-MINER PoC v3.2.5

## Installazione del front-end

La versione v3.2.5 modifica esclusivamente il front-end del dashboard.

Sul Server B eseguire:

```bash
cd pcb-dashboard/server-b
chmod +x install-v3.2.5-ui-only.sh
sudo DASHBOARD_PATH=/var/www/html/pcb-dashboard ./install-v3.2.5-ui-only.sh
```

Lo script verifica il file sorgente, crea un backup dell'eventuale dashboard esistente, installa `index.html` in modo atomico e controlla lo SHA-256 del file installato.

Lo script non riavvia e non ricarica nginx, il master node, il verifier o altri servizi HashBurst.

SHA-256 atteso del front-end v3.2.5:

```text
6bed070b47386997bb6c67c3eb7f1f3252beb39206905c87d16382f26a06c013
```

Dopo l'installazione verificare il dashboard dal browser e forzare il ricaricamento della cache se necessario.

## Front-end installation

Version v3.2.5 changes only the dashboard front end.

On Server B run:

```bash
cd pcb-dashboard/server-b
chmod +x install-v3.2.5-ui-only.sh
sudo DASHBOARD_PATH=/var/www/html/pcb-dashboard ./install-v3.2.5-ui-only.sh
```

The script validates the source file, creates a backup of any existing dashboard, installs `index.html` atomically and verifies the SHA-256 of the installed file.

The script does not restart or reload nginx, the master node, the verifier or any other HashBurst service.
