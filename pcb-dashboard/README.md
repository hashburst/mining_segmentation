# HashBurst TEP-MINER PCB Dashboard

Front-end della Proof of Concept HashBurst DePIN TEP-MINER.

## Scopo della PoC

Questa Proof of Concept è stata sviluppata per studiare il possibile funzionamento e verificare la fattibilità tecnica della realizzazione di PCB dedicate come nodi di un cluster di calcolo distribuito orchestrato da sistemi AI basati su intelligenza artificiale. Nell'architettura considerata, il master node è un server HPC incaricato del coordinamento del cluster, dell'assegnazione dei segmenti di lavoro, della raccolta dei risultati e dell'integrazione con i servizi di mining. Un esempio di master node è un HPE Cray XD675 con 9 acceleratori AMD Instinct MI300, raggiungibile all'indirizzo IP 85.233.199.35.

La PoC è destinata alla verifica tecnica dell'architettura e dei flussi tra master node, nodi PCB, protocollo TEP, attività di hashing e servizi di mining. Non costituisce una dichiarazione di prestazioni della futura PCB né una garanzia di redditività del mining.

## Purpose of the PoC

This Proof of Concept was developed to study the possible operating model and verify the technical feasibility of dedicated PCBs acting as nodes of a distributed computing cluster orchestrated by AI systems based on artificial intelligence. In the architecture considered by the PoC, the master node is an HPC server responsible for cluster coordination, work segment assignment, result collection and integration with mining services. An example master node is an HPE Cray XD675 with 9 AMD Instinct MI300 accelerators, reachable at IP address 85.233.199.35.

The PoC is intended for technical validation of the architecture and of the flows between the master node, PCB nodes, TEP protocol, hashing activity and mining services. It does not constitute a performance statement for the future PCB and does not guarantee mining profitability.

## Versione

La versione corrente del front-end è v3.2.5.

La v3.2.5 parte dalla baseline v3.2.4 e modifica esclusivamente gli elementi dell'interfaccia richiesti per la rappresentazione dei contatori di esperimento e per la denominazione dei nodi sottoposti ad audit.

Il file `server-b/index.html` è il front-end di riferimento e non deve essere modificato durante le operazioni di installazione o pubblicazione.

SHA-256 di `server-b/index.html`:

```text
6bed070b47386997bb6c67c3eb7f1f3252beb39206905c87d16382f26a06c013
```

## Contenuto

`server-b/index.html` contiene il dashboard.

`server-b/install-v3.2.5-ui-only.sh` installa il dashboard sul Server B senza riavviare nginx o altri servizi HashBurst.

`evidence/audited-evidence.json` contiene le evidenze di audit incluse nel pacchetto.

`SOURCE-PROVENANCE.md` documenta la baseline e gli hash del front-end.

`CHANGELOG.md` registra le modifiche della versione.

## Installazione sul Server B

```bash
cd pcb-dashboard/server-b
chmod +x install-v3.2.5-ui-only.sh
sudo DASHBOARD_PATH=/var/www/html/pcb-dashboard ./install-v3.2.5-ui-only.sh
```

Lo script esegue il backup dell'eventuale `index.html` presente, installa il nuovo file in modo atomico e verifica il relativo SHA-256. Non riavvia e non ricarica nginx o altri servizi HashBurst.
