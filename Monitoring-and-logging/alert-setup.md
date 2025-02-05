<h2>Set Up Alerting</h2>
* create "alert.rule.yml" where you created the prometheus.yml file
<code>
groups:
  - name: jenkins_alerts
    rules:
      - alert: JenkinsDown
        expr: up{job="jenkins"} == 0
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Jenkins instance is down"
</code>
* start alertmanager by runnning <code>./alertmanager --config.file=alertmanager.yml
</code>
* setup alerts in grafana
<code>menu > Alerting > Notification channels > add your reuired alert method like email or anything.</code>
