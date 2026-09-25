---
modified: 2026-09-23T23:37:35+03:00
---
something repeatedly taking too long
    
- something requiring unnecessary manual work
    
- someone maintaining a spreadsheet nobody likes
    
- information being copied between systems
    
- people using WhatsApp because the official system is inadequate
    
- someone checking something manually every day
    
- a technician repeatedly diagnosing the same failure
    
- a business owner saying “there has to be an easier way”
    
- a process dependent on one knowledgeable employee
    
- a task requiring annoying coordination

- complaints
    
- negative reviews
    
- support questions
    
- Reddit discussions
    
- forum threads
    
- Stack Overflow questions
    
- “how do I…” searches
    
- troubleshooting guides
    
- YouTube repair videos
    
- job descriptions
    
- job ads
    
- regulatory documents
    
- procurement specifications
    
- maintenance logs
    
- incident reports
    
- FAQ pages
    
- feature requests
    
- software changelogs
    
- “known issues”
    
- workarounds
- dle labor
    
- rework
    
- rejected jobs
    
- missed appointments
    
- inventory discrepancies
    
- unnecessary purchases
    
- downtime
    
- overtime
    
- duplicated data entry
    
- billing delays
    
- quotation delays
    
- abandoned leads
    
- failed handoffs
    
- preventable maintenance
    
- customer churn caused by service problems
new reporting requirements
    
- documentation requirements
    
- audit trails
    
- certification
    
- inspections
    
- record retention
    
- safety procedures
    
- environmental reporting
    
- AI governance
    
- cybersecurity requirements
    
- industry-specific compliance
    

The interesting structure is:

> **New obligation → new workflow → new recurring burden → new tooling opportunity**

**World → Sensors → Observations → Problem Candidates → Validation → Problem Graph → Opportunity Generation**

We look for situations where a new capability changes the **cost structure of solving old problems**.

For example:

> Computer vision becomes cheap enough to inspect objects automatically.

Then search:

> What inspection problems were previously too expensive to automate?

Or:

> Browser agents become capable of navigating complicated websites.

Then:

> What human workflows exist primarily because websites cannot be operated programmatically?

Or:

> Cheap local AI inference becomes practical.

Then:

> What information-processing workflows currently cannot use cloud AI because of privacy, latency, connectivity, or cost constraints?

This generates **problem spaces from technological change**, rather than extracting them from existing complaints.

Job descriptions are enormous databases of organizational problems disguised as hiring requirements.

A company hiring:

> “Operations Coordinator — responsible for manually reconciling X, Y and Z across multiple systems”

is effectively saying:

> **We currently have a human-shaped hole in this workflow.**

Repeated job descriptions can reveal:

- recurring organizational tasks
    
- emerging responsibilities
    
- expensive human bottlenecks
    
- skills companies cannot easily find
    
- workflows being created by technological change
    

Instead of asking:

> “What jobs are growing?”

the Atlas asks:

> **“What organizational problems are repeatedly expensive enough to justify hiring someone?”**

ome problems aren't really inside an organization.

They occur **between organizations**.

Examples:

> manufacturer ↔ distributor  
> contractor ↔ supplier  
> hospital ↔ laboratory  
> freelancer ↔ client  
> landlord ↔ maintenance provider  
> factory ↔ external technician

Look for:

- information asymmetry
    
- missing information
    
- coordination delays
    
- incompatible formats
    
- scheduling problems
    
- verification problems
    
- trust problems
    
- responsibility ambiguity
    
- repeated phone calls
    
- duplicated data
    

These inter-organizational boundaries are particularly fertile because nobody necessarily owns the entire workflow.

The Atlas should accept:

> **“That's weird. Why do they do it that way?”**

without requiring an immediate business case.

Examples:

- bizarre industrial processes
    
- strange interfaces
    
- obsolete technologies still widely used
    
- elaborate manual rituals
    
- unusual physical tools
    
- businesses with strange economics
    
- industries operating differently from adjacent industries
    
- practices that seem technologically behind
    

The system records the anomaly.

Later, other nodes may connect to it.

This is where **serendipitous discovery** enters the architecture.

OBSERVATION

What happened:
A technician spends ~20 minutes reconstructing previous job information
from WhatsApp messages, photographs and handwritten notes.

Context:
Commercial installation / maintenance

Actors:
Technician
Office administrator
Customer

Evidence:
Direct observation

Frequency:
Repeated

Why interesting:
Information exists but is fragmented across channels.

Unknown:
How common is this workflow?
How costly is it?
What systems are already used?
```

Only later does the system transform it into:

```text
PROBLEM

Fragmented historical job information forces technicians
to reconstruct context manually before beginning work.
```

And only later:

```text
PROBLEM CLUSTER

Field-service organizations frequently maintain operational
knowledge across disconnected communication channels,
creating recurring reconstruction and handoff costs.
```

And only later:

```text
OPPORTUNITY HYPOTHESIS

A system that automatically reconstructs job context from
existing communication and documentation may reduce
technician preparation and handoff time.
```


The complete architecture becomes:

```text
                         REAL WORLD
                             │
          ┌──────────────────┼──────────────────┐
          ↓                  ↓                  ↓
      Direct Work       Digital Research    Technology
      Observation       / Complaints        Changes
          │                  │                  │
          ↓                  ↓                  ↓
      Workflows         Failures            New
      / Friction         / Gaps          Capabilities
          │                  │                  │
          └──────────────────┼──────────────────┘
                             ↓
                    OBSERVATION STORE
                             │
                    pattern detection
                             ↓
                     PROBLEM CANDIDATES
                             │
                  evidence / repetition
                             ↓
                     PROBLEM GRAPH
                             │
              ┌──────────────┼──────────────┐
              ↓              ↓              ↓
          Industries      Actors       Workflows
              │              │              │
              └──────────────┼──────────────┘
                             ↓
                    OPPORTUNITY SPACES
                             │
                             ↓
                    IDEA GENERATION
                             │
                             ↓
                       RESEARCH
                             │
                             ↓
                    NEW OBSERVATIONS
                             │
                             └──────────────→ GRAPH
```