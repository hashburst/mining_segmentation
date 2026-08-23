# HashBurst Mining Segmentation

Repository della Proof of Concept HashBurst dedicata alla segmentazione del lavoro di mining e alla distribuzione di intervalli di nonce tra più nodi di calcolo.

## Scopo della PoC

Questa Proof of Concept è stata sviluppata per studiare il possibile funzionamento e verificare la fattibilità tecnica della realizzazione di PCB dedicate come nodi di un cluster di calcolo distribuito orchestrato da sistemi AI basati su intelligenza artificiale. Nell'architettura considerata, il master node è un server HPC incaricato del coordinamento del cluster, dell'assegnazione dei segmenti di lavoro, della raccolta dei risultati e dell'integrazione con i servizi di mining. Un esempio di master node è un HPE Cray XD675 con 8 acceleratori AMD Instinct MI300, raggiungibile all'indirizzo IP 85.233.199.35.

La PoC serve a verificare il modello tecnico, i flussi di comunicazione, la segmentazione del lavoro, il coordinamento dei nodi e la possibilità di utilizzare PCB dedicate come componenti di un cluster eterogeneo. Non costituisce una dichiarazione di prestazioni della futura PCB né una garanzia di redditività del mining.

## Purpose of the PoC

This Proof of Concept was developed to study the possible operating model and verify the technical feasibility of dedicated PCBs acting as nodes of a distributed computing cluster orchestrated by AI systems based on artificial intelligence. In the architecture considered by the PoC, the master node is an HPC server responsible for cluster coordination, work segment assignment, result collection and integration with mining services. An example master node is an HPE Cray XD675 with 8 AMD Instinct MI300 accelerators, reachable at IP address 85.233.199.35.

The PoC is intended to validate the technical model, communication flows, work segmentation, node coordination and the possible use of dedicated PCBs as components of a heterogeneous cluster. It does not constitute a performance statement for the future PCB and does not guarantee mining profitability.

## Architettura tecnica

Il master node divide lo spazio di ricerca in segmenti e assegna ogni intervallo a un nodo disponibile. I nodi elaborano in modo indipendente il segmento ricevuto e restituiscono i risultati al master node. Il coordinamento può utilizzare informazioni sullo stato dei nodi, sulla capacità di calcolo, sulla latenza e sul carico per modificare l'assegnazione del lavoro.

La cartella `block_segmentation` contiene un esempio minimale in Python del modello master e worker. La cartella `pcb-dashboard` contiene il front-end della PoC TEP-MINER e i file di installazione relativi alla versione corrente.

## Esecuzione locale dell'esempio di segmentazione

Avviare il master:

```bash
cd block_segmentation
python3 master.py
```

Avviare uno o più worker in terminali separati:

```bash
cd block_segmentation
python3 worker.py
```

L'esempio locale è dimostrativo e utilizza parametri semplificati. La PoC TEP-MINER utilizza componenti e flussi distinti descritti nella relativa documentazione.
