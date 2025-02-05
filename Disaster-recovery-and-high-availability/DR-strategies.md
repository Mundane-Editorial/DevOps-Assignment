This document is all about the Disaster Recovery (DR) strategy to keep our cloud apps up and running, making sure they’re reliable and can bounce back when something goes wrong. We’ll break down the Recovery Time Objective (RTO) and Recovery Point Objective (RPO), along with our backup rules and failover plans.

* RECOVERY OBJECTIVES
it define the tolerances for downtime (RTO) and data loss (RPO) in case of a system failure or disaster. which helps to determine the appropriate disaster recovery (DR) strategy, infrastructure investments, and backup policies.

1. Recovery time Objective (RTO)
    RTO is all about how long an app or system can be down before it needs to be back up and running. If you want a shorter RTO, you'll need a lot more backup systems and some cool automatic switches to get things running again. But if you can wait a bit longer, you can do it the old-school way and save some cash. 
    * Mission-Critical Applications : the applications which must be restored almost immediately to avoid severe business impact. eg: payment sites
    * High-Priority Applications : important applications that should recover quickly but can tolerate short downtime. eg: social media sites
    * Standard Applications : Business applications that can tolerate a few hours of downtime. eg: business portfolio
    * Low-Priority Applications :  applications that can be restored later with minimal impact. eg: personal portfolios etc.

2. Recovery Point Objective (RPO)
    RPO is basically the most data your app can lose without messing up business stuff. It also tells you how often you need to back things up. If you want a lower RPO, you'll be backing up more often and maybe even doing real-time replication, which can jack up your storage and infrastructure costs.
    * Transaction-Critical Applications : which handles real time transactions where datalosses are strictly unacceptable. eg: banks.
    * Regular Business Applications : these are application where small downtime is acceptable. eg: CRMs.
    * non-critical appliation : Applications where a full-day loss of data does not significantly impact operations. eg: data warehousing


