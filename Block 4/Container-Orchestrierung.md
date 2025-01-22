### Auftrag 4.1: Container-Orchestrierung
- Warum braucht man Container-Orchestrierung?

    - Automatisieren von Deployment, Management, Skalierung nd Vernetzung von Containern während ihres gesamten Lifecycles.
    [RedHAT](https://www.redhat.com/de/topics/containers/what-is-container-orchestration#:~:text=Die%20Container-Orchestrierung%20bezeichnet%20den%20Prozess%20zum%20Automatisieren%20von,Umgebungen%20einsetzen%2C%20ohne%20sie%20neu%20konzipieren%20zu%20m%C3%BCssen.)
1. **Warum braucht man Container-Orchestrierung?**
   Container-Orchestrierung automatisiert die Verwaltung und Koordination von Container-basierten Anwendungen. Sie hilft bei der Bereitstellung, Skalierung, Lastverteilung, Fehlerbehebung, Netzwerk- und Speicherverwaltung sowie dem Konfigurationsmanagement. Ein bekanntes Tool dafür ist [Kubernetes](https://kubernetes.io/).

2. **Wie funktioniert Container-Orchestrierung?**
   Container-Orchestrierungstools wie Kubernetes ermöglichen es, Container-Anwendungen automatisch bereitzustellen und zu skalieren. Sie verteilen den Netzwerkverkehr gleichmäßig auf die Container, erkennen fehlerhafte Container und starten sie neu, verwalten Konfigurationsdaten und Geheimnisse, und sorgen für eine effiziente Kommunikation zwischen den Containern.

3. **Welche Container-Orchestrierung Technologien kennen Sie?**
   Einige der bekanntesten Container-Orchestrierungstechnologien sind:
   - **Kubernetes**: Ein weit verbreitetes Open-Source-Orchestrierungstool.
   - **Docker Swarm**: Eine native Orchestrierungslösung von Docker.
   - **Apache Mesos**: Ein verteiltes System für die Verwaltung von Rechenressourcen.
   - **Amazon ECS (Elastic Container Service)**: Ein von AWS angebotener Orchestrierungsdienst.

4. **Was versteht man unter "Scaling Containers"?**
   "Scaling Containers" bezieht sich auf die Fähigkeit, die Anzahl der laufenden Container dynamisch zu erhöhen oder zu verringern, um den Anforderungen gerecht zu werden. Dies kann automatisch basierend auf der aktuellen Last oder manuell durch den Administrator erfolgen.

5. **Was gibt es für Deployment Strategien?**
   Es gibt verschiedene Deployment-Strategien für Container-Anwendungen, darunter:
   - **Rolling Updates**: Container werden nacheinander aktualisiert, um Ausfallzeiten zu minimieren.
   - **Blue-Green Deployment**: Zwei identische Umgebungen (blau und grün) werden verwendet, um nahtlose Updates zu ermöglichen.
   - **Canary Deployment**: Neue Versionen werden schrittweise eingeführt, um die Auswirkungen auf die Benutzer zu minimieren.
   - **A/B Testing**: Verschiedene Versionen der Anwendung werden gleichzeitig getestet, um die beste Leistung zu ermitteln.

